# Nombre: studio.py
# Fecha: 2026-06-29
# Utilidad: launcher CLI inicial de SkillOAF Studio.
# API/Funcion asociada: StudioSession / ProcessEngine / ProcessLoader.
# Descripcion: inicia el microkernel, ejecuta un workflow base o un proceso declarativo JSON y muestra estado ejecutivo por consola.
# Uso: python studio.py --project . --process processes/templates/flujo_base.json
# Resultado esperado: Kernel iniciado, proceso ejecutado y artefactos generados en output/.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

import argparse
import json
from pathlib import Path

from processes.engine import ProcessEngine
from processes.loader import ProcessLoader
from runtime.session import StudioSession


def imprimir_resumen(session: StudioSession, results: list) -> None:
    print("SkillOAF Studio 0.2")
    print("Kernel iniciado")
    print("Runtime Fase A iniciado")
    print("ProcessEngine integrado")

    print("\nResultados:")
    for result in results:
        estado = "OK" if result.ok else "ERROR"
        print(f"- {result.agent_name}: {estado} - {result.message}")

    print("\nAgentes registrados:")
    for agent in session.kernel.agents.list_agents():
        print(f"- {agent}")

    print("\nArtefactos:")
    for kind, paths in session.kernel.artifacts.as_dict().items():
        print(f"- {kind}: {len(paths)}")

    print("\nMetricas:")
    for key, value in session.kernel.metrics.snapshot().items():
        print(f"- {key}: {value}")


def resolver_process_path(project: Path, process_arg: str | None) -> Path | None:
    if not process_arg:
        default = session_default_process(project)
        return default if default.exists() else None
    process_path = Path(process_arg)
    return process_path if process_path.is_absolute() else project / process_path


def session_default_process(project: Path) -> Path:
    return project / "processes" / "templates" / "flujo_base.json"


def main() -> int:
    parser = argparse.ArgumentParser(description="SkillOAF Studio CLI")
    parser.add_argument("--project", default=".", help="Carpeta raiz del proyecto")
    parser.add_argument("--process", help="Archivo JSON de proceso declarativo")
    parser.add_argument("--status-json", action="store_true", help="Imprime estado completo en JSON")
    args = parser.parse_args()

    project_root = Path(args.project).resolve()
    session = StudioSession(project_root)
    session.start()

    process_path = resolver_process_path(project_root, args.process)
    if process_path is not None:
        data = ProcessLoader.load_json(process_path)
        engine = ProcessEngine(session)
        results = engine.run_dict(data)
    else:
        results = session.run_default_workflow()

    imprimir_resumen(session, results)

    if args.status_json:
        print("\nEstado JSON:")
        print(json.dumps(session.status(), indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
