# Nombre: dispatcher.py
# Fecha: 2026-06-29
# Utilidad: despachador de tareas hacia agentes en SkillOAF Studio.
# API/Funcion asociada: Dispatcher.dispatch.
# Descripcion: toma una RuntimeTask y la envia al Kernel para que el AgentBus ejecute el agente correspondiente.
# Uso: dispatcher.dispatch(task)
# Resultado esperado: AgentResult generado y evento runtime_task_completed publicado.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from core.agent_bus import AgentResult
from core.kernel import Kernel
from runtime.task_queue import RuntimeTask


class Dispatcher:
    def __init__(self, kernel: Kernel) -> None:
        self.kernel = kernel

    def dispatch(self, task: RuntimeTask) -> AgentResult:
        task.status = "running"
        self.kernel.events.publish(
            "runtime_task_started",
            {"task_id": task.task_id, "agent": task.agent, "action": task.action},
        )
        result = self.kernel.run_agent(
            task.agent,
            {"action": task.action, "task_id": task.task_id, **task.payload},
        )
        task.status = "completed" if result.ok else "failed"
        self.kernel.events.publish(
            "runtime_task_completed",
            {
                "task_id": task.task_id,
                "agent": task.agent,
                "action": task.action,
                "ok": result.ok,
                "message": result.message,
            },
        )
        return result
