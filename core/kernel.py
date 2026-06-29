# Nombre: kernel.py
# Fecha: 2026-06-29
# Utilidad: nucleo principal de SkillOAF Studio.
# API/Funcion asociada: Kernel.boot / Kernel.register_default_agents / Kernel.status.
# Descripcion: coordina EventBus, MemoryBus, AgentBus y ArtifactEngine como microkernel inicial.
# Uso: kernel = Kernel('.'); kernel.boot(); print(kernel.status())
# Resultado esperado: kernel iniciado con buses, memoria, agentes desacoplados y artefactos basicos.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from agents.backend_agent import BackendAgent
from agents.coordinador_agent import CoordinadorAgent
from agents.frontend_agent import FrontendAgent
from core.agent_bus import AgentBus, AgentResult
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
        for agent in (CoordinadorAgent(), FrontendAgent(), BackendAgent()):
            agent.initialize(self)
            self.agents.register(agent)

    def run_agent(self, agent_name: str, payload: Dict[str, Any] | None = None) -> AgentResult:
        return self.agents.dispatch(agent_name, payload or {})

    def status(self) -> Dict[str, Any]:
        return {
            "booted": self.booted,
            "project_root": str(self.project_root),
            "agents": self.agents.list_agents(),
            "memory": self.memory.all(),
            "decisions": self.memory.decisions,
            "assumptions": self.memory.assumptions,
            "pending": self.memory.pending,
            "artifacts": self.artifacts.as_dict(),
            "events": [event.name for event in self.events.history],
        }
