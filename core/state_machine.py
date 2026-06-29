# Nombre: state_machine.py
# Fecha: 2026-06-29
# Utilidad: maquina de estados oficial para SkillOAF Studio.
# API/Funcion asociada: StateMachine.transition_to / can_transition.
# Descripcion: controla transiciones validas del ciclo de vida operativo del proyecto y del Kernel.
# Uso: sm = StateMachine(); sm.transition_to('project_loaded')
# Resultado esperado: estado actualizado solo si la transicion es valida.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Set


@dataclass
class StateChange:
    previous: str
    current: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


class StateMachine:
    VALID_TRANSITIONS: Dict[str, Set[str]] = {
        "new": {"booting", "error"},
        "booting": {"booted", "error"},
        "booted": {"project_loaded", "error"},
        "project_loaded": {"analyzing", "planning", "ready", "error"},
        "analyzing": {"planning", "error"},
        "planning": {"generating", "error"},
        "generating": {"validating", "error"},
        "validating": {"documenting", "ready", "error"},
        "documenting": {"ready", "error"},
        "ready": {"analyzing", "planning", "generating", "closed", "error"},
        "closed": {"project_loaded"},
        "error": {"booting", "project_loaded", "closed"},
    }

    def __init__(self) -> None:
        self.current = "new"
        self.history: List[StateChange] = []

    def can_transition(self, target: str) -> bool:
        return target in self.VALID_TRANSITIONS.get(self.current, set())

    def transition_to(self, target: str) -> None:
        if not self.can_transition(target):
            raise ValueError(f"Transicion invalida: {self.current} -> {target}")
        previous = self.current
        self.current = target
        self.history.append(StateChange(previous=previous, current=target))

    def snapshot(self) -> dict:
        return {
            "current": self.current,
            "history": [change.__dict__ for change in self.history],
        }
