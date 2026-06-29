# Nombre: parser.py
# Fecha: 2026-06-29
# Utilidad: parser simple para procesos declarativos SkillOAF.
# API/Funcion asociada: ProcessParser.parse_dict.
# Descripcion: convierte diccionarios Python en ProcessDefinition sin dependencias externas.
# Uso: ProcessParser.parse_dict({'name':'crud','steps':[{'agent':'frontend'}]})
# Resultado esperado: ProcessDefinition listo para compilar a Workflow.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Any, Dict

from processes.process_model import ProcessDefinition, ProcessStep


class ProcessParser:
    @staticmethod
    def parse_dict(data: Dict[str, Any]) -> ProcessDefinition:
        steps = []
        for item in data.get("steps", []):
            if isinstance(item, str):
                steps.append(ProcessStep(agent=item))
            else:
                steps.append(
                    ProcessStep(
                        agent=item.get("agent", "coordinador"),
                        action=item.get("action", "run"),
                        payload=item.get("payload", {}),
                    )
                )

        return ProcessDefinition(
            name=data.get("name", "proceso_sin_nombre"),
            version=data.get("version", "0.1.0"),
            description=data.get("description", ""),
            steps=steps,
        )
