# Nombre: memory_bus.py
# Fecha: 2026-06-29
# Utilidad: memoria interna del proyecto para SkillOAF Studio.
# API/Funcion asociada: MemoryBus.set / MemoryBus.get / MemoryBus.append_decision.
# Descripcion: administra memoria funcional, tecnica, historica y ejecutiva del proyecto.
# Uso: memory.set('stack.frontend','Flet'); memory.get('stack.frontend')
# Resultado esperado: lectura y escritura simple de memoria del proyecto.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List


@dataclass
class MemoryEntry:
    key: str
    value: Any
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


class MemoryBus:
    def __init__(self) -> None:
        self._store: Dict[str, MemoryEntry] = {}
        self.decisions: List[str] = []
        self.assumptions: List[str] = []
        self.pending: List[str] = []

    def set(self, key: str, value: Any) -> None:
        self._store[key] = MemoryEntry(key=key, value=value)

    def get(self, key: str, default: Any = None) -> Any:
        entry = self._store.get(key)
        return entry.value if entry else default

    def all(self) -> Dict[str, Any]:
        return {key: entry.value for key, entry in self._store.items()}

    def append_decision(self, text: str) -> None:
        self.decisions.append(text)

    def append_assumption(self, text: str) -> None:
        self.assumptions.append(text)

    def append_pending(self, text: str) -> None:
        self.pending.append(text)
