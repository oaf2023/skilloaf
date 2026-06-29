# Nombre: kernel.py
# Fecha: 2026-06-29
# Utilidad: nucleo principal de SkillOAF Studio.
# API/Funcion asociada: Kernel.boot / Kernel.register_default_agents / Kernel.status.
# Descripcion: coordina EventBus, MemoryBus, AgentBus, ArtifactEngine, configuracion, logs y metricas.
# Uso: kernel = Kernel('.'); kernel.boot(); print(kernel.status())
# Resultado esperado: kernel iniciado con buses, memoria, agentes desacoplados, artefactos, logs y metricas.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from agents.backend_agent import BackendAgent
from agents.coordinador_agent import CoordinadorAgent
from agents.database_agent import DatabaseAgent
from agents.devops_agent import DevOpsAgent
from agents.frontend_agent import FrontendAgent
from agents.qa_agent import QAAgent
from core.agent_bus import AgentBus, AgentResult
from core.artifact_engine import ArtifactEngine
from core.configuration import ConfigurationManager
from core.event_bus import EventBus
from core.logging_engine import LoggingEngine
from core.memory_bus import MemoryBus
from core.metrics import MetricsEngine


class Kernel:
    def __init__(self, project_root: str | Path = ".") -> None:
        self.project_root = Path(project_root).resolve()
        self.config = ConfigurationManager()
        self.logger = LoggingEngine(self.project_root)
        self.metrics = MetricsEngine()
        self.events = EventBus()
        self.memory = MemoryBus()
        self.agents = AgentBus()
        self.artifacts = ArtifactEngine(self.project_root)
        self.booted = False

    def boot(self) -> None:
        self.project_root.mkdir(parents=True, exist_ok=True)
        self.memory.set("kernel.name", "SkillOAF Studio")
        self.memory.set("kernel.version", "0.2.0")
        self.memory.set("project.root", str(self.project_root))
        self.metrics.increment("kernel.boot.count")
        self.register_default_agents()
        self.events.publish("kernel_booted", {"project_root": str(self.project_root)})
        self.logger.info("Kernel iniciado")
        self.booted = True

    def register_default_agents(self) -> None:
        agents = (
            CoordinadorAgent(),
            FrontendAgent(),
            BackendAgent(),
            DatabaseAgent(),
            QAAgent(),
            DevOpsAgent(),
        )
        for agent in agents:
            agent.initialize(self)
            self.agents.register(agent)
            self.metrics.increment("agents.registered")

    def run_agent(self, agent_name: str, payload: Dict[str, Any] | None = None) -> AgentResult:
        result = self.agents.dispatch(agent_name, payload or {})
        self.metrics.increment("agents.completed" if result.ok else "agents.failed")
        self.logger.info(f"Agente ejecutado: {agent_name} ok={result.ok}")
        return result

    def status(self) -> Dict[str, Any]:
        return {
            "booted": self.booted,
            "project_root": str(self.project_root),
            "config": self.config.all(),
            "agents": self.agents.list_agents(),
            "memory": self.memory.all(),
            "decisions": self.memory.decisions,
            "assumptions": self.memory.assumptions,
            "pending": self.memory.pending,
            "artifacts": self.artifacts.as_dict(),
            "events": [event.name for event in self.events.history],
            "metrics": self.metrics.snapshot(),
            "logs": [entry.__dict__ for entry in self.logger.entries],
        }
