# Nombre: base_agent.py
# Fecha: 2026-06-29
# Utilidad: clase base para agentes especialistas de SkillOAF Studio.
# API/Funcion asociada: BaseAgent.initialize / BaseAgent.handle / BaseAgent.shutdown.
# Descripcion: define contrato comun para agentes desacoplados conectados al Kernel por AgentBus.
# Uso: class MiAgent(BaseAgent): ...; agent.initialize(kernel)
# Resultado esperado: agentes con interfaz uniforme, rol, version y ciclo de vida.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from core.agent_bus import AgentResult, AgentTask


class BaseAgent(ABC):
    name: str = "base"
    role: str = "Agente base"
    version: str = "0.1.0"

    def __init__(self) -> None:
        self.kernel: Optional[Any] = None
        self.initialized: bool = False

    def initialize(self, kernel: Any) -> None:
        self.kernel = kernel
        self.initialized = True
        if hasattr(kernel, "events"):
            kernel.events.publish("agent_initialized", {"agent": self.name, "role": self.role})

    def can_handle(self, task: AgentTask) -> bool:
        return task.target == self.name

    @abstractmethod
    def handle(self, task: AgentTask) -> AgentResult:
        raise NotImplementedError

    def shutdown(self) -> None:
        if self.kernel and hasattr(self.kernel, "events"):
            self.kernel.events.publish("agent_shutdown", {"agent": self.name})
        self.initialized = False

    def ok(self, message: str, data: Dict[str, Any] | None = None) -> AgentResult:
        return AgentResult(agent_name=self.name, ok=True, message=message, data=data or {})

    def fail(self, message: str, data: Dict[str, Any] | None = None) -> AgentResult:
        return AgentResult(agent_name=self.name, ok=False, message=message, data=data or {})
