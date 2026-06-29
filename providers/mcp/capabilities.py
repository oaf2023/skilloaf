# Nombre: capabilities.py
# Fecha: 2026-06-29
# Utilidad: modelo de capacidades MCP para SkillOAF Studio.
# API/Funcion asociada: MCPCapability.
# Descripcion: representa capacidades declaradas por un servidor MCP o conector equivalente.
# Uso: MCPCapability(name='github.search', kind='tool')
# Resultado esperado: capacidad instanciada y registrable.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class MCPCapability:
    name: str
    kind: str
    description: str = ""
    metadata: Dict[str, Any] | None = None

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "kind": self.kind,
            "description": self.description,
            "metadata": self.metadata or {},
        }
