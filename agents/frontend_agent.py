# Nombre: frontend_agent.py
# Fecha: 2026-06-29
# Utilidad: agente frontend desacoplado de SkillOAF Studio.
# API/Funcion asociada: FrontendAgent.handle.
# Descripcion: genera artefactos iniciales de frontend y deja contratos visuales basicos.
# Uso: agent = FrontendAgent(); agent.initialize(kernel); agent.handle(task)
# Resultado esperado: output/frontend/README_FRONTEND.md generado.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from core.agent_bus import AgentResult, AgentTask
from agents.base_agent import BaseAgent


class FrontendAgent(BaseAgent):
    name = "frontend"
    role = "Genera pantallas, componentes, layout y contratos visuales"
    version = "0.1.0"

    def handle(self, task: AgentTask) -> AgentResult:
        if not self.kernel:
            return self.fail("Kernel no inicializado")

        self.kernel.artifacts.write(
            "output/frontend/README_FRONTEND.md",
            "# Frontend\n\n"
            "## Objetivo\n\n"
            "Generar la capa visual del proyecto manteniendo separacion estricta del backend.\n\n"
            "## Pendientes\n\n"
            "- Leer requirements/project_requirements.yaml.\n"
            "- Generar ui_schema.yaml.\n"
            "- Generar pantallas base.\n",
            "frontend",
            self.name,
        )
        self.kernel.events.publish("agent_completed", {"agent": self.name})
        return self.ok("Artefacto frontend generado")
