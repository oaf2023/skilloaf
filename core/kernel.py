# Nombre: kernel.py
# Fecha: 2026-06-29
# Utilidad: nucleo principal de SkillOAF Studio.
# API/Funcion asociada: Kernel.boot / Kernel.register_default_agents / Kernel.status.
# Descripcion: coordina EventBus, MemoryBus, AgentBus y ArtifactEngine como microkernel inicial.
# Uso: kernel = Kernel('.'); kernel.boot(); print(kernel.status())
# Resultado esperado: kernel iniciado con buses, memoria, agentes y artefactos basicos.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from core.agent_bus import AgentBus, AgentResult, AgentTask, FunctionAgent
from core.artifact_engine import ArtifactEngine
from core.event_bus import EventBus
from core.memory_bus import MemoryBus


class Kernel:
    def __init__(self, project_root: str | Path = ".") -> None:
        self.project_root = Path(project_root).resolve()
        self.events = EventBus()
        self.memory = MemoryBus()
        self.agents = AgentBus()
        self.artifacts = ArtifactEngine(self.project_root)
        self.booted = False

    def boot(self) -> None:
        self.project_root.mkdir(parents=True, exist_ok=True)
        self.memory.set("kernel.name", "SkillOAF Studio")
        self.memory.set("kernel.version", "0.1.0")
        self.memory.set("project.root", str(self.project_root))
        self.register_default_agents()
        self.events.publish("kernel_booted", {"project_root": str(self.project_root)})
        self.booted = True

    def register_default_agents(self) -> None:
        self.agents.register(FunctionAgent("coordinador", "Coordina el flujo general", self._agent_coordinador))
        self.agents.register(FunctionAgent("frontend", "Genera artefactos frontend", self._agent_frontend))
        self.agents.register(FunctionAgent("backend", "Genera artefactos backend", self._agent_backend))

    def _agent_coordinador(self, task: AgentTask) -> AgentResult:
        self.memory.append_decision("El coordinador valido el flujo inicial del proyecto.")
        self.artifacts.write(
            "output/docs/PLAN_EJECUCION.md",
            "# Plan de ejecucion\n\n- Validar gobierno.\n- Ejecutar Frontend.\n- Ejecutar Backend.\n- Consolidar artefactos.\n",
            "documentacion",
            "coordinador",
        )
        self.events.publish("agent_completed", {"agent": "coordinador"})
        return AgentResult("coordinador", True, "Plan de ejecucion generado")

    def _agent_frontend(self, task: AgentTask) -> AgentResult:
        self.artifacts.write(
            "output/frontend/README_FRONTEND.md",
            "# Frontend\n\nArtefacto inicial generado por el agente frontend.\n",
            "frontend",
            "frontend",
        )
        self.events.publish("agent_completed", {"agent": "frontend"})
        return AgentResult("frontend", True, "Artefacto frontend generado")

    def _agent_backend(self, task: AgentTask) -> AgentResult:
        self.artifacts.write(
            "output/backend/README_BACKEND.md",
            "# Backend\n\nArtefacto inicial generado por el agente backend.\n",
            "backend",
            "backend",
        )
        self.events.publish("agent_completed", {"agent": "backend"})
        return AgentResult("backend", True, "Artefacto backend generado")

    def run_agent(self, agent_name: str, payload: Dict[str, Any] | None = None) -> AgentResult:
        return self.agents.dispatch(agent_name, payload or {})

    def status(self) -> Dict[str, Any]:
        return {
            "booted": self.booted,
            "project_root": str(self.project_root),
            "agents": self.agents.list_agents(),
            "memory": self.memory.all(),
            "artifacts": self.artifacts.as_dict(),
            "events": [event.name for event in self.events.history],
        }
