# Nombre: session.py
# Fecha: 2026-06-29
# Utilidad: sesion operativa de SkillOAF Studio.
# API/Funcion asociada: StudioSession.start / StudioSession.run_workflow.
# Descripcion: encapsula Kernel, TaskQueue, Dispatcher y Scheduler para ejecutar workflows.
# Uso: session = StudioSession('.'); session.start(); session.run_default_workflow()
# Resultado esperado: kernel iniciado y agentes ejecutados segun workflow.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from pathlib import Path
from typing import List

from core.agent_bus import AgentResult
from core.kernel import Kernel
from runtime.dispatcher import Dispatcher
from runtime.scheduler import Scheduler
from runtime.task_queue import TaskQueue
from runtime.workflow import Workflow


class StudioSession:
    def __init__(self, project_root: str | Path = ".") -> None:
        self.project_root = Path(project_root).resolve()
        self.kernel = Kernel(self.project_root)
        self.queue = TaskQueue()
        self.dispatcher = Dispatcher(self.kernel)
        self.scheduler = Scheduler(self.queue, self.dispatcher)

    def start(self) -> None:
        self.kernel.boot()
        self.kernel.events.publish("studio_session_started", {"project_root": str(self.project_root)})

    def run_workflow(self, workflow: Workflow) -> List[AgentResult]:
        self.kernel.events.publish("workflow_started", {"name": workflow.name})
        workflow.enqueue(self.queue)
        results = self.scheduler.run_until_empty()
        self.kernel.events.publish("workflow_completed", {"name": workflow.name, "results": len(results)})
        return results

    def run_default_workflow(self) -> List[AgentResult]:
        workflow = Workflow.from_agents("flujo_base", ["coordinador", "frontend", "backend"])
        return self.run_workflow(workflow)

    def status(self) -> dict:
        base = self.kernel.status()
        base["queue_size"] = self.queue.size()
        base["completed_results"] = [result.__dict__ for result in self.scheduler.completed]
        return base
