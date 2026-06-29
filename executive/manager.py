# Nombre: manager.py
# Fecha: 2026-06-29
# Utilidad: Director del Proyecto para SkillOAF Studio.
# API/Funcion asociada: ExecutiveManager.execute_goal.
# Descripcion: recibe un objetivo ejecutivo, selecciona proceso, ejecuta ProcessEngine y devuelve resumen de negocio.
# Uso: manager = ExecutiveManager('.'); manager.execute_goal('crear crud de clientes')
# Resultado esperado: proceso ejecutado y resumen con resultados, contexto y artefactos.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from executive.context_engine import ContextEngine
from executive.decision_engine import DecisionEngine
from executive.goal_engine import GoalEngine
from executive.planner import ExecutivePlanner
from processes.engine import ProcessEngine
from processes.loader import ProcessLoader
from runtime.session import StudioSession


class ExecutiveManager:
    def __init__(self, project_root: str | Path = ".") -> None:
        self.session = StudioSession(project_root)
        self.goal_engine = GoalEngine()
        self.planner = ExecutivePlanner()
        self.started = False

    def start(self) -> None:
        if not self.started:
            self.session.start()
            self.started = True

    def execute_goal(self, goal: str) -> Dict[str, Any]:
        self.start()
        kernel = self.session.kernel
        classification = self.goal_engine.classify(goal)
        plan = self.planner.build_plan(classification)
        decision = DecisionEngine(kernel)
        process_path = decision.select_process_path(str(plan["process_name"]))
        absolute_process_path = kernel.project_root / process_path
        data = ProcessLoader.load_json(absolute_process_path)
        results = ProcessEngine(self.session).run_dict(data)
        context = ContextEngine(kernel).snapshot()

        kernel.memory.append_decision(f"ExecutiveManager ejecuto objetivo: {goal}")
        kernel.events.publish("executive_goal_completed", {"goal": goal, "process": str(plan["process_name"])})
        kernel.logger.info(f"Objetivo ejecutivo completado: {goal}")

        return {
            "goal": goal,
            "classification": classification,
            "plan": plan,
            "results": [result.__dict__ for result in results],
            "context": context,
            "status": kernel.status(),
        }
