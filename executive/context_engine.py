# Nombre: context_engine.py
# Fecha: 2026-06-29
# Utilidad: motor de contexto ejecutivo para SkillOAF Studio.
# API/Funcion asociada: ContextEngine.snapshot.
# Descripcion: arma una vista ejecutiva compacta del estado actual del Kernel para decisiones del Director.
# Uso: ContextEngine(kernel).snapshot()
# Resultado esperado: dict con proyecto, estado, agentes y catalogo.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Any, Dict


class ContextEngine:
    def __init__(self, kernel: Any) -> None:
        self.kernel = kernel

    def snapshot(self) -> Dict[str, Any]:
        return {
            "project": self.kernel.project.snapshot(),
            "state": self.kernel.state.snapshot(),
            "agents": self.kernel.agent_registry.snapshot(),
            "processes": self.kernel.process_catalog.snapshot(),
            "metrics": self.kernel.metrics.snapshot(),
        }
