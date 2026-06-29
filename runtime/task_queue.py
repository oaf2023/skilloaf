# Nombre: task_queue.py
# Fecha: 2026-06-29
# Utilidad: cola de tareas para el runtime de SkillOAF Studio.
# API/Funcion asociada: TaskQueue.push / TaskQueue.pop / TaskQueue.is_empty.
# Descripcion: administra tareas pendientes para que el scheduler las ejecute mediante agentes.
# Uso: queue.push(RuntimeTask(agent='frontend', action='generar'))
# Resultado esperado: tarea encolada y disponible para despacho.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Deque, Dict, Optional
from uuid import uuid4


@dataclass
class RuntimeTask:
    agent: str
    action: str
    payload: Dict[str, Any] = field(default_factory=dict)
    task_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    status: str = "pending"


class TaskQueue:
    def __init__(self) -> None:
        self._queue: Deque[RuntimeTask] = deque()

    def push(self, task: RuntimeTask) -> RuntimeTask:
        self._queue.append(task)
        return task

    def pop(self) -> Optional[RuntimeTask]:
        if not self._queue:
            return None
        return self._queue.popleft()

    def is_empty(self) -> bool:
        return not self._queue

    def size(self) -> int:
        return len(self._queue)

    def snapshot(self) -> list[dict[str, Any]]:
        return [task.__dict__.copy() for task in self._queue]
