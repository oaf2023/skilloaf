# Nombre: agent_service.py
# Fecha: 2026-06-29
# Utilidad: servicio permanente de administracion de agentes en SkillOAF Studio.
# API/Funcion asociada: AgentService.register_defaults / run.
# Descripcion: encapsula registro y ejecucion de agentes para desacoplarlos del Kernel.
# Uso: service = AgentService(kernel); service.register_defaults(); service.run('frontend')
# Resultado esperado: agentes registrados y ejecutables desde servicio.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Any, Dict


class AgentService:
    name = "agent"

    def __init__(self, kernel: Any) -> None:
        self.kernel = kernel
        self.started = False

    def start(self) -> None:
        self.started = True

    def stop(self) -> None:
        self.started = False

    def register_defaults(self) -> None:
        for agent in self.kernel.agent_registry.create_all():
            agent.initialize(self.kernel)
            self.kernel.agents.register(agent)
            self.kernel.metrics.increment("agents.registered")

    def run(self, agent_name: str, payload: Dict[str, Any] | None = None) -> Any:
        return self.kernel.run_agent(agent_name, payload or {})

    def status(self) -> Dict[str, Any]:
        return {
            "started": self.started,
            "registered_agents": self.kernel.agents.list_agents(),
            "catalog_agents": self.kernel.agent_registry.snapshot(),
        }
