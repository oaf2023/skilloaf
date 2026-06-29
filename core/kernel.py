# Nombre: kernel.py
# Fecha: 2026-06-29
# Utilidad: nucleo principal de SkillOAF Studio.
# API/Funcion asociada: Kernel.boot / Kernel.register_default_agents / Kernel.status.
# Descripcion: coordina buses, memoria, agentes, artefactos, configuracion, logs, metricas, proyecto, estados, catalogos y servicios.
# Uso: kernel = Kernel('.'); kernel.boot(); print(kernel.status())
# Resultado esperado: kernel iniciado con servicios disponibles en kernel.services, incluyendo MCPService.
# Conexion API: no conecta a APIs externas; MCPService esta preparado como canal de integracion.

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from agents.registry import AgentRegistry
from core.agent_bus import AgentBus, AgentResult
from core.artifact_engine import ArtifactEngine
from core.configuration import ConfigurationManager
from core.event_bus import EventBus
from core.logging_engine import LoggingEngine
from core.memory_bus import MemoryBus
from core.metrics import MetricsEngine
from core.project_manager import ProjectManager
from core.state_machine import StateMachine
from processes.catalog import ProcessCatalog
from services.agent_service import AgentService
from services.artifact_service import ArtifactService
from services.knowledge_service import KnowledgeService
from services.mcp_service import MCPService
from services.process_service import ProcessService
from services.project_service import ProjectService
from services.service_manager import ServiceManager


class Kernel:
    def __init__(self, project_root: str | Path = ".") -> None:
        self.project_root = Path(project_root).resolve()
        self.config = ConfigurationManager()
        self.logger = LoggingEngine(self.project_root)
        self.metrics = MetricsEngine()
        self.state = StateMachine()
        self.project = ProjectManager(self.project_root)
        self.agent_registry = AgentRegistry.default()
        self.process_catalog = ProcessCatalog.default()
        self.events = EventBus()
        self.memory = MemoryBus()
        self.agents = AgentBus()
        self.artifacts = ArtifactEngine(self.project_root)
        self.services = ServiceManager(self)
        self.booted = False
        self.register_foundational_services()

    def register_foundational_services(self) -> None:
        self.services.register("project", ProjectService(self))
        self.services.register("agent", AgentService(self))
        self.services.register("process", ProcessService(self))
        self.services.register("artifact", ArtifactService(self))
        self.services.register("knowledge", KnowledgeService(self))
        self.services.register("mcp", MCPService(self))

    def boot(self) -> None:
        self.state.transition_to("booting")
        self.services.start_all()
        metadata = self.services.get("project").open()
        self.memory.set("kernel.name", "SkillOAF Studio")
        self.memory.set("kernel.version", "0.4.0")
        self.memory.set("project.root", str(self.project_root))
        self.memory.set("project.name", metadata["name"])
        self.metrics.increment("kernel.boot.count")
        self.register_default_agents()
        self.events.publish("kernel_booted", {"project_root": str(self.project_root)})
        self.logger.info("Kernel iniciado")
        self.state.transition_to("booted")
        self.state.transition_to("project_loaded")
        self.booted = True

    def register_default_agents(self) -> None:
        self.services.get("agent").register_defaults()

    def bind_session(self, session: Any) -> None:
        self.services.get("process").bind_session(session)

    def run_agent(self, agent_name: str, payload: Dict[str, Any] | None = None) -> AgentResult:
        result = self.agents.dispatch(agent_name, payload or {})
        self.metrics.increment("agents.completed" if result.ok else "agents.failed")
        self.logger.info(f"Agente ejecutado: {agent_name} ok={result.ok}")
        return result

    def status(self) -> Dict[str, Any]:
        return {
            "booted": self.booted,
            "project": self.project.snapshot(),
            "project_root": str(self.project_root),
            "state": self.state.snapshot(),
            "services": self.services.snapshot(),
            "config": self.config.all(),
            "agent_registry": self.agent_registry.snapshot(),
            "process_catalog": self.process_catalog.snapshot(),
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
