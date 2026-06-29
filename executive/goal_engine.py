# Nombre: goal_engine.py
# Fecha: 2026-06-29
# Utilidad: motor de interpretacion de objetivos para el Director del Proyecto.
# API/Funcion asociada: GoalEngine.classify.
# Descripcion: clasifica pedidos ejecutivos simples y sugiere proceso objetivo.
# Uso: GoalEngine().classify('crear crud de clientes')
# Resultado esperado: dict con goal_type y process_name.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Dict


class GoalEngine:
    def classify(self, goal: str) -> Dict[str, str]:
        text = goal.lower().strip()
        if "crud" in text or "abm" in text:
            return {"goal_type": "crud", "process_name": "flujo_base"}
        if "erp" in text:
            return {"goal_type": "erp", "process_name": "flujo_base"}
        if "crm" in text or "clientes" in text:
            return {"goal_type": "crm", "process_name": "flujo_base"}
        return {"goal_type": "general", "process_name": "flujo_base"}
