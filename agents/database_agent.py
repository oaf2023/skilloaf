# Nombre: database_agent.py
# Fecha: 2026-06-29
# Utilidad: agente database desacoplado de SkillOAF Studio.
# API/Funcion asociada: DatabaseAgent.handle.
# Descripcion: genera artefactos iniciales de base de datos, schema SQL y lineamientos de migracion.
# Uso: agent = DatabaseAgent(); agent.initialize(kernel); agent.handle(task)
# Resultado esperado: output/database/schema.sql y README_DATABASE.md generados.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from core.agent_bus import AgentResult, AgentTask
from agents.base_agent import BaseAgent


class DatabaseAgent(BaseAgent):
    name = "database"
    role = "Diseña modelo de datos, SQL, indices y migraciones"
    version = "0.1.0"

    def handle(self, task: AgentTask) -> AgentResult:
        if not self.kernel:
            return self.fail("Kernel no inicializado")

        self.kernel.artifacts.write(
            "output/database/README_DATABASE.md",
            "# Database\n\n"
            "## Objetivo\n\n"
            "Generar el modelo de datos, claves, indices y migraciones del proyecto.\n\n"
            "## Pendientes\n\n"
            "- Leer requirements/project_requirements.yaml.\n"
            "- Detectar entidades maestras y transaccionales.\n"
            "- Preparar SQLite para prototipo y PostgreSQL para produccion.\n",
            "database",
            self.name,
        )
        self.kernel.artifacts.write(
            "output/database/schema.sql",
            "-- Schema inicial generado por DatabaseAgent\n"
            "-- Pendiente: completar a partir de requirements/project_requirements.yaml\n\n"
            "CREATE TABLE IF NOT EXISTS auditoria_eventos (\n"
            "    id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
            "    entidad TEXT NOT NULL,\n"
            "    accion TEXT NOT NULL,\n"
            "    detalle TEXT,\n"
            "    creado_en TEXT DEFAULT CURRENT_TIMESTAMP\n"
            ");\n",
            "database",
            self.name,
        )
        self.kernel.events.publish("agent_completed", {"agent": self.name})
        return self.ok("Artefactos database generados")
