# Nombre: backend_agent.py
# Fecha: 2026-06-29
# Utilidad: agente backend desacoplado de SkillOAF Studio.
# API/Funcion asociada: BackendAgent.handle.
# Descripcion: genera artefactos iniciales de backend y deja contratos de servicios basicos.
# Uso: agent = BackendAgent(); agent.initialize(kernel); agent.handle(task)
# Resultado esperado: output/backend/README_BACKEND.md generado.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from core.agent_bus import AgentResult, AgentTask
from agents.base_agent import BaseAgent


class BackendAgent(BaseAgent):
    name = "backend"
    role = "Genera APIs, servicios, modelos y contratos backend"
    version = "0.1.0"

    def handle(self, task: AgentTask) -> AgentResult:
        if not self.kernel:
            return self.fail("Kernel no inicializado")

        self.kernel.artifacts.write(
            "output/backend/README_BACKEND.md",
            "# Backend\n\n"
            "## Objetivo\n\n"
            "Generar la capa de servicios, APIs y reglas de negocio del proyecto.\n\n"
            "## Pendientes\n\n"
            "- Leer requirements/project_requirements.yaml.\n"
            "- Generar modelos y schemas.\n"
            "- Generar endpoints base.\n",
            "backend",
            self.name,
        )
        self.kernel.events.publish("agent_completed", {"agent": self.name})
        return self.ok("Artefacto backend generado")
