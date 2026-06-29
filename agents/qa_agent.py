# Nombre: qa_agent.py
# Fecha: 2026-06-29
# Utilidad: agente QA desacoplado de SkillOAF Studio.
# API/Funcion asociada: QAAgent.handle.
# Descripcion: genera artefactos iniciales de pruebas, criterios de calidad y checklist operativo.
# Uso: agent = QAAgent(); agent.initialize(kernel); agent.handle(task)
# Resultado esperado: output/tests/PLAN_QA.md generado.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from core.agent_bus import AgentResult, AgentTask
from agents.base_agent import BaseAgent


class QAAgent(BaseAgent):
    name = "qa"
    role = "Define pruebas, calidad, validaciones y criterios de aceptacion"
    version = "0.1.0"

    def handle(self, task: AgentTask) -> AgentResult:
        if not self.kernel:
            return self.fail("Kernel no inicializado")

        self.kernel.artifacts.write(
            "output/tests/PLAN_QA.md",
            "# Plan QA\n\n"
            "## Objetivo\n\n"
            "Validar que los artefactos generados sean consistentes, ejecutables y alineados al requerimiento.\n\n"
            "## Checklist inicial\n\n"
            "- Verificar existencia de datos.md, memoria.md y reglas.md.\n"
            "- Verificar requirements/project_requirements.yaml.\n"
            "- Validar separacion frontend/backend/database.\n"
            "- Validar que los scripts Python tengan encabezado.\n"
            "- Validar existencia de pruebas minimas por modulo.\n",
            "tests",
            self.name,
        )
        self.kernel.events.publish("agent_completed", {"agent": self.name})
        return self.ok("Plan QA generado")
