# Nombre: registry.py
# Fecha: 2026-06-29
# Utilidad: registro formal de agentes especialistas de SkillOAF Studio.
# API/Funcion asociada: AgentRegistry.register / create_all.
# Descripcion: centraliza definicion, version, rol y factory de agentes disponibles.
# Uso: registry = AgentRegistry.default(); agents = registry.create_all()
# Resultado esperado: agentes instanciados para registrar en Kernel.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List, Type

from agents.backend_agent import BackendAgent
from agents.base_agent import BaseAgent
from agents.coordinador_agent import CoordinadorAgent
from agents.database_agent import DatabaseAgent
from agents.devops_agent import DevOpsAgent
from agents.frontend_agent import FrontendAgent
from agents.qa_agent import QAAgent


@dataclass
class AgentDescriptor:
    name: str
    role: str
    version: str
    factory: Callable[[], BaseAgent]


class AgentRegistry:
    def __init__(self) -> None:
        self._items: Dict[str, AgentDescriptor] = {}

    def register(self, agent_cls: Type[BaseAgent]) -> None:
        descriptor = AgentDescriptor(
            name=agent_cls.name,
            role=agent_cls.role,
            version=agent_cls.version,
            factory=agent_cls,
        )
        self._items[descriptor.name] = descriptor

    def create(self, name: str) -> BaseAgent:
        if name not in self._items:
            raise KeyError(f"Agente no registrado: {name}")
        return self._items[name].factory()

    def create_all(self) -> List[BaseAgent]:
        return [descriptor.factory() for descriptor in self._items.values()]

    def names(self) -> List[str]:
        return sorted(self._items.keys())

    def snapshot(self) -> List[dict]:
        return [
            {"name": item.name, "role": item.role, "version": item.version}
            for item in self._items.values()
        ]

    @classmethod
    def default(cls) -> "AgentRegistry":
        registry = cls()
        for agent_cls in (
            CoordinadorAgent,
            FrontendAgent,
            BackendAgent,
            DatabaseAgent,
            QAAgent,
            DevOpsAgent,
        ):
            registry.register(agent_cls)
        return registry
