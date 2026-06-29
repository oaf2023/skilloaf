# Nombre: test_basico.py
# Fecha: 2026-06-29
# Utilidad: prueba basica integral de SkillOAF Studio.
# API/Funcion asociada: StudioSession / ProcessService / MCPService.
# Descripcion: valida arranque del Kernel, servicios, agentes, proceso base, artefactos y MCP placeholder.
# Uso: python tests/test_basico.py
# Resultado esperado: OK - prueba basica completada.
# Conexion API: no conecta a APIs externas; MCP usa cliente placeholder.

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.session import StudioSession


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    project_root = ROOT / "tmp_test_project"
    session = StudioSession(project_root)
    session.start()

    kernel = session.kernel

    assert_true(kernel.booted, "Kernel no inicio")
    assert_true("project" in kernel.services.names(), "ProjectService no registrado")
    assert_true("agent" in kernel.services.names(), "AgentService no registrado")
    assert_true("process" in kernel.services.names(), "ProcessService no registrado")
    assert_true("artifact" in kernel.services.names(), "ArtifactService no registrado")
    assert_true("knowledge" in kernel.services.names(), "KnowledgeService no registrado")
    assert_true("mcp" in kernel.services.names(), "MCPService no registrado")

    results = session.run_default_workflow()
    assert_true(len(results) == 6, "El workflow base no ejecuto 6 agentes")
    assert_true(all(result.ok for result in results), "Alguno de los agentes fallo")

    artifacts = kernel.artifacts.as_dict()
    assert_true("frontend" in artifacts, "No se genero artefacto frontend")
    assert_true("backend" in artifacts, "No se genero artefacto backend")
    assert_true("database" in artifacts, "No se genero artefacto database")
    assert_true("tests" in artifacts, "No se genero artefacto QA/tests")
    assert_true("deploy" in artifacts, "No se genero artefacto deploy")

    mcp = kernel.services.get("mcp")
    mcp.register_server("demo", "stdio://demo")
    mcp.register_capability("demo", "demo.echo", "tool", "Herramienta simulada de prueba")
    response = mcp.call_tool("demo", "demo.echo", {"mensaje": "hola"})
    assert_true(response["ok"], "MCP placeholder no respondio OK")

    status = session.status()
    assert_true(status["state"]["current"] == "project_loaded", "Estado final inesperado")
    assert_true(status["metrics"].get("agents.completed", 0) >= 6, "Metricas de agentes incompletas")

    print("OK - prueba basica completada")
    print(f"Proyecto temporal: {project_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
