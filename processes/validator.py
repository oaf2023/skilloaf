# Nombre: validator.py
# Fecha: 2026-06-29
# Utilidad: validador de procesos declarativos para SkillOAF Studio.
# API/Funcion asociada: ProcessValidator.validate.
# Descripcion: valida que un proceso tenga nombre, pasos y agentes registrados cuando se provee Kernel.
# Uso: ProcessValidator.validate(process, kernel)
# Resultado esperado: lista de errores; lista vacia si el proceso es valido.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Any, List

from processes.process_model import ProcessDefinition


class ProcessValidator:
    @staticmethod
    def validate(process: ProcessDefinition, kernel: Any | None = None) -> List[str]:
        errors: List[str] = []

        if not process.name.strip():
            errors.append("El proceso no tiene nombre.")

        if not process.steps:
            errors.append("El proceso no tiene pasos.")

        if kernel is not None:
            registered = set(kernel.agents.list_agents())
            for index, step in enumerate(process.steps, start=1):
                if step.agent not in registered:
                    errors.append(f"Paso {index}: agente no registrado: {step.agent}")

        return errors
