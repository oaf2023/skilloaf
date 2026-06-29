# Nombre: engine.py
# Fecha: 2026-06-29
# Utilidad: motor de procesos declarativos para SkillOAF Studio.
# API/Funcion asociada: ProcessEngine.run_dict.
# Descripcion: parsea, valida, compila y ejecuta procesos usando StudioSession.
# Uso: ProcessEngine(session).run_dict({'name':'base','steps':['coordinador','frontend']})
# Resultado esperado: proceso ejecutado por Runtime y resultados de agentes devueltos.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Any, Dict, List

from core.agent_bus import AgentResult
from processes.compiler import ProcessCompiler
from processes.parser import ProcessParser
from processes.validator import ProcessValidator
from runtime.session import StudioSession


class ProcessEngine:
    def __init__(self, session: StudioSession) -> None:
        self.session = session

    def run_dict(self, data: Dict[str, Any]) -> List[AgentResult]:
        process = ProcessParser.parse_dict(data)
        errors = ProcessValidator.validate(process, self.session.kernel)
        if errors:
            joined = "; ".join(errors)
            raise ValueError(f"Proceso invalido: {joined}")

        workflow = ProcessCompiler.to_workflow(process)
        return self.session.run_workflow(workflow)
