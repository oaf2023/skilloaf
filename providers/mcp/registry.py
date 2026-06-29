# Nombre: registry.py
# Fecha: 2026-06-29
# Utilidad: registro de servidores y capacidades MCP para SkillOAF Studio.
# API/Funcion asociada: MCPRegistry.register_server / register_capability.
# Descripcion: mantiene inventario local de servidores MCP y capacidades disponibles.
# Uso: registry.register_server('github', 'stdio://github'); registry.register_capability('github', cap)
# Resultado esperado: servidores y capacidades disponibles para MCPService.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from providers.mcp.capabilities import MCPCapability


@dataclass
class MCPServerDescriptor:
    name: str
    endpoint: str
    enabled: bool = True
    capabilities: List[MCPCapability] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "endpoint": self.endpoint,
            "enabled": self.enabled,
            "capabilities": [cap.as_dict() for cap in self.capabilities],
        }


class MCPRegistry:
    def __init__(self) -> None:
        self._servers: Dict[str, MCPServerDescriptor] = {}

    def register_server(self, name: str, endpoint: str, enabled: bool = True) -> None:
        self._servers[name] = MCPServerDescriptor(name=name, endpoint=endpoint, enabled=enabled)

    def register_capability(self, server_name: str, capability: MCPCapability) -> None:
        if server_name not in self._servers:
            raise KeyError(f"Servidor MCP no registrado: {server_name}")
        self._servers[server_name].capabilities.append(capability)

    def get_server(self, name: str) -> MCPServerDescriptor:
        if name not in self._servers:
            raise KeyError(f"Servidor MCP no registrado: {name}")
        return self._servers[name]

    def list_servers(self) -> List[str]:
        return sorted(self._servers.keys())

    def snapshot(self) -> List[dict]:
        return [server.as_dict() for server in self._servers.values()]
