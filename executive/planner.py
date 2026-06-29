# Nombre: planner.py
# Fecha: 2026-06-29
# Utilidad: planificador ejecutivo para SkillOAF Studio.
# API/Funcion asociada: ExecutivePlanner.build_plan.
# Descripcion: transforma un objetivo clasificado en un plan de ejecucion con proceso y pasos ejecutivos.
# Uso: ExecutivePlanner().build_plan({'goal_type':'crud','process_name':'flujo_base'})
# Resultado esperado: dict con plan ejecutivo.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Dict, List


class ExecutivePlanner:
    def build_plan(self, classification: Dict[str, str]) -> Dict[str, object]:
        process_name = classification.get("process_name", "flujo_base")
        return {
            "process_name": process_name,
            "goal_type": classification.get("goal_type", "general"),
            "steps": [
                "abrir_proyecto",
                "validar_gobierno",
                "seleccionar_proceso",
                "ejecutar_runtime",
                "registrar_resultados",
                "reportar_estado",
            ],
        }
