# Nombre: loader.py
# Fecha: 2026-06-29
# Utilidad: cargador de procesos declarativos JSON para SkillOAF Studio.
# API/Funcion asociada: ProcessLoader.load_json.
# Descripcion: lee archivos JSON de procesos y devuelve diccionarios listos para ProcessEngine.
# Uso: data = ProcessLoader.load_json('processes/templates/flujo_base.json')
# Resultado esperado: dict con name, version, description y steps.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


class ProcessLoader:
    @staticmethod
    def load_json(path: str | Path) -> Dict[str, Any]:
        target = Path(path)
        if not target.exists():
            raise FileNotFoundError(f"No existe el proceso: {target}")
        return json.loads(target.read_text(encoding="utf-8"))
