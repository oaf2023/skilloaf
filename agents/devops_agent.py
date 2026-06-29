# Nombre: devops_agent.py
# Fecha: 2026-06-29
# Utilidad: agente DevOps desacoplado de SkillOAF Studio.
# API/Funcion asociada: DevOpsAgent.handle.
# Descripcion: genera artefactos iniciales de despliegue, entorno y automatizacion.
# Uso: agent = DevOpsAgent(); agent.initialize(kernel); agent.handle(task)
# Resultado esperado: output/deploy/README_DEPLOY.md y .env.example generados.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from core.agent_bus import AgentResult, AgentTask
from agents.base_agent import BaseAgent


class DevOpsAgent(BaseAgent):
    name = "devops"
    role = "Prepara despliegue, entorno, Docker y automatizacion"
    version = "0.1.0"

    def handle(self, task: AgentTask) -> AgentResult:
        if not self.kernel:
            return self.fail("Kernel no inicializado")

        self.kernel.artifacts.write(
            "output/deploy/README_DEPLOY.md",
            "# Deploy\n\n"
            "## Objetivo\n\n"
            "Preparar la ejecucion local, futura contenerizacion y despliegue del proyecto.\n\n"
            "## Pendientes\n\n"
            "- Definir puertos.\n"
            "- Definir variables de entorno.\n"
            "- Preparar Docker Compose.\n"
            "- Preparar scripts de inicio.\n",
            "deploy",
            self.name,
        )
        self.kernel.artifacts.write(
            "output/deploy/.env.example",
            "APP_NAME=SkillOAF_Project\n"
            "APP_ENV=local\n"
            "DATABASE_URL=sqlite:///app.db\n"
            "SECRET_KEY=change_me\n",
            "deploy",
            self.name,
        )
        self.kernel.events.publish("agent_completed", {"agent": self.name})
        return self.ok("Artefactos DevOps generados")
