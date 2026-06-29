# Nombre: process_model.py
# Fecha: 2026-06-29
# Utilidad: modelos de proceso declarativo para SkillOAF Studio.
# API/Funcion asociada: ProcessDefinition / ProcessStep.
# Descripcion: define estructuras basicas para representar procesos reutilizables.
# Uso: ProcessDefinition(name='crud', steps=[ProcessStep(agent='frontend')])
# Resultado esperado: modelo de proceso instanciado.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ProcessStep:
    agent: str
    action: str = "run"
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ProcessDefinition:
    name: str
    version: str = "0.1.0"
    description: str = ""
    steps: List[ProcessStep] = field(default_factory=list)
