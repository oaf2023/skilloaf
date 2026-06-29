# Nombre: agent_bus.py
# Fecha: 2026-06-29
# Utilidad: bus de agentes para SkillOAF Studio.
# API/Funcion asociada: AgentBus.register / AgentBus.dispatch.
# Descripcion: registra agentes especialistas y despacha tareas de forma desacoplada.
# Uso: bus.register(agent); bus.dispatch('frontend', {'accion':'generar_ui'})
# Resultado esperado: el agente asignado procesa la tarea y devuelve un resultado.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List, Protocol


@dataclass
class AgentTask:
    target: str
    payload: Dict[str, Any]
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


@dataclass
class AgentResult:
    agent_name: str
    ok: bool
    message: str
    data: Dict[str, Any] = field(default_factory=dict)


class Agent(Protocol):
    name: str
    role: str

    def handle(self, task: AgentTask) -> AgentResult:
        ...


class FunctionAgent:
    def __init__(self, name: str, role: str, handler: Callable[[AgentTask], AgentResult]) -> None:
        self.name = name
        self.role = role
        self._handler = handler

    def handle(self, task: AgentTask) -> AgentResult:
        return self._handler(task)


class AgentBus:
    def __init__(self) -> None:
        self._agents: Dict[str, Agent] = {}
        self.history: List[AgentResult] = []

    def register(self, agent: Agent) -> None:
        self._agents[agent.name] = agent

    def list_agents(self) -> List[str]:
        return sorted(self._agents.keys())

    def dispatch(self, target: str, payload: Dict[str, Any] | None = None) -> AgentResult:
        if target not in self._agents:
            result = AgentResult(agent_name=target, ok=False, message="Agente no registrado")
            self.history.append(result)
            return result

        task = AgentTask(target=target, payload=payload or {})
        result = self._agents[target].handle(task)
        self.history.append(result)
        return result
