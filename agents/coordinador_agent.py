# Nombre: coordinador_agent.py
# Fecha: 2026-06-29
# Utilidad: agente coordinador desacoplado de SkillOAF Studio.
# API/Funcion asociada: CoordinadorAgent.handle.
# Descripcion: valida el flujo inicial, registra decisiones y genera el plan de ejecucion del proyecto.
# Uso: agent = CoordinadorAgent(); agent.initialize(kernel); agent.handle(task)
# Resultado esperado: output/docs/PLAN_EJECUCION.md generado.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from core.agent_bus import AgentResult, AgentTask
from agents.base_agent import BaseAgent


class CoordinadorAgent(BaseAgent):
    name = "coordinador"
    role = "Coordina flujo, consistencia y plan de ejecucion"
    version = "0.1.0"

    def handle(self, task: AgentTask) -> AgentResult:
        if not self.kernel:
            return self.fail("Kernel no inicializado")

        self.kernel.memory.append_decision("El Coordinador valido el flujo inicial del proyecto.")
        self.kernel.artifacts.write(
            "output/docs/PLAN_EJECUCION.md",
            "# Plan de ejecucion\n\n"
            "## Orden operativo\n\n"
            "1. Validar gobierno documental.\n"
            "2. Ejecutar agente Frontend.\n"
            "3. Ejecutar agente Backend.\n"
            "4. Consolidar artefactos.\n"
            "5. Registrar supuestos y pendientes.\n",
            "documentacion",
            self.name,
        )
        self.kernel.events.publish("agent_completed", {"agent": self.name})
        return self.ok("Plan de ejecucion generado")
