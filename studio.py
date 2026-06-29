# Nombre: studio.py
# Fecha: 2026-06-29
# Utilidad: launcher CLI inicial de SkillOAF Studio.
# API/Funcion asociada: StudioSession.
# Descripcion: inicia el microkernel, ejecuta un workflow base y muestra estado ejecutivo por consola.
# Uso: python studio.py --project .
# Resultado esperado: Kernel iniciado, agentes ejecutados y artefactos generados en output/.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

import argparse
import json
from pathlib import Path

from runtime.session import StudioSession


def main() -> int:
    parser = argparse.ArgumentParser(description="SkillOAF Studio CLI")
    parser.add_argument("--project", default=".", help="Carpeta raiz del proyecto")
    parser.add_argument("--status-json", action="store_true", help="Imprime estado completo en JSON")
    args = parser.parse_args()

    session = StudioSession(Path(args.project))
    session.start()
    results = session.run_default_workflow()

    print("SkillOAF Studio 0.1")
    print("Kernel iniciado")
    print("Runtime Fase A iniciado")
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

    if args.status_json:
        print("\nEstado JSON:")
        print(json.dumps(session.status(), indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
