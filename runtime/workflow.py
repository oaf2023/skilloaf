# Nombre: workflow.py
# Fecha: 2026-06-29
# Utilidad: motor de workflows declarativos para SkillOAF Studio.
# API/Funcion asociada: Workflow.from_agents / Workflow.enqueue.
# Descripcion: convierte una secuencia de agentes en tareas ejecutables por el runtime.
# Uso: Workflow.from_agents('crud', ['coordinador','frontend']).enqueue(queue)
# Resultado esperado: tareas encoladas para ejecucion por scheduler.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List

from runtime.task_queue import RuntimeTask, TaskQueue


@dataclass
class WorkflowStep:
    agent: str
    action: str = "run"
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Workflow:
    name: str
    steps: List[WorkflowStep]

    @classmethod
    def from_agents(cls, name: str, agents: List[str]) -> "Workflow":
        return cls(name=name, steps=[WorkflowStep(agent=agent) for agent in agents])

    def enqueue(self, queue: TaskQueue) -> List[RuntimeTask]:
        tasks: List[RuntimeTask] = []
        for step in self.steps:
            task = RuntimeTask(agent=step.agent, action=step.action, payload=step.payload)
            queue.push(task)
            tasks.append(task)
        return tasks
