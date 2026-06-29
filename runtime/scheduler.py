# Nombre: scheduler.py
# Fecha: 2026-06-29
# Utilidad: planificador de tareas para SkillOAF Studio.
# API/Funcion asociada: Scheduler.run_until_empty.
# Descripcion: consume tareas de TaskQueue y las ejecuta mediante Dispatcher.
# Uso: scheduler.run_until_empty()
# Resultado esperado: tareas pendientes ejecutadas en orden.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

import sys
from concurrent.futures import ThreadPoolExecutor
from typing import List

from core.agent_bus import AgentResult
from runtime.dispatcher import Dispatcher
from runtime.task_queue import TaskQueue, RuntimeTask


class Scheduler:
    def __init__(self, queue: TaskQueue, dispatcher: Dispatcher) -> None:
        self.queue = queue
        self.dispatcher = dispatcher
        self.completed: List[AgentResult] = []

    def run_until_empty(self) -> List[AgentResult]:
        pending: List[RuntimeTask] = []
        while not self.queue.is_empty():
            task = self.queue.pop()
            if task is not None:
                pending.append(task)

        if sys.version_info > (3, 13) and len(pending) > 1:
            with ThreadPoolExecutor() as executor:
                self.completed.extend(executor.map(self.dispatcher.dispatch, pending))
        else:
            for task in pending:
                self.completed.append(self.dispatcher.dispatch(task))

        return self.completed
