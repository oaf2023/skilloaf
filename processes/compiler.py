# Nombre: compiler.py
# Fecha: 2026-06-29
# Utilidad: compilador de ProcessDefinition a Workflow runtime.
# API/Funcion asociada: ProcessCompiler.to_workflow.
# Descripcion: convierte procesos declarativos en workflows ejecutables por Runtime.
# Uso: workflow = ProcessCompiler.to_workflow(process)
# Resultado esperado: Workflow listo para StudioSession.run_workflow.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from processes.process_model import ProcessDefinition
from runtime.workflow import Workflow, WorkflowStep


class ProcessCompiler:
    @staticmethod
    def to_workflow(process: ProcessDefinition) -> Workflow:
        return Workflow(
            name=process.name,
            steps=[
                WorkflowStep(agent=step.agent, action=step.action, payload=step.payload)
                for step in process.steps
            ],
        )
