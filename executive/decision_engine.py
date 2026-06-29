# Nombre: decision_engine.py
# Fecha: 2026-06-29
# Utilidad: motor de decisiones ejecutivo para SkillOAF Studio.
# API/Funcion asociada: DecisionEngine.select_process_path.
# Descripcion: selecciona la ruta del proceso a ejecutar a partir del catalogo del Kernel.
# Uso: DecisionEngine(kernel).select_process_path('flujo_base')
# Resultado esperado: ruta relativa del proceso declarativo.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from pathlib import Path
from typing import Any


class DecisionEngine:
    def __init__(self, kernel: Any) -> None:
        self.kernel = kernel

    def select_process_path(self, process_name: str) -> Path:
        item = self.kernel.process_catalog.get(process_name)
        return Path(item.path)
