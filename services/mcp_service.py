# Nombre: mcp_service.py
# Fecha: 2026-06-29
# Utilidad: servicio permanente de integracion MCP para SkillOAF Studio.
# API/Funcion asociada: MCPService.register_server / call_tool.
# Descripcion: administra servidores MCP, sesiones y llamadas a tools sin exponer MCP directamente a agentes ni Kernel.
# Uso: service.register_server('github','stdio://github'); service.call_tool('github','search', {'q':'demo'})
# Resultado esperado: llamada MCP canalizada por servicio con contrato uniforme.
# Conexion API: preparado para MCP; cliente actual es placeholder sin transporte real.

from __future__ import annotations

from typing import Any, Dict

from providers.mcp.capabilities import MCPCapability
from providers.mcp.registry import MCPRegistry
from providers.mcp.session import MCPSession


class MCPService:
    name = "mcp"

    def __init__(self, kernel: Any) -> None:
        self.kernel = kernel
        self.started = False
        self.registry = MCPRegistry()
        self.sessions: Dict[str, MCPSession] = {}

    def start(self) -> None:
        self.started = True

    def stop(self) -> None:
        for session in self.sessions.values():
            session.close()
        self.sessions.clear()
        self.started = False

    def register_server(self, name: str, endpoint: str, enabled: bool = True) -> None:
        self.registry.register_server(name, endpoint, enabled)
        self.kernel.events.publish("mcp_server_registered", {"name": name, "endpoint": endpoint})

    def register_capability(self, server_name: str, name: str, kind: str, description: str = "") -> None:
        self.registry.register_capability(
            server_name,
            MCPCapability(name=name, kind=kind, description=description),
        )
        self.kernel.events.publish("mcp_capability_registered", {"server": server_name, "capability": name})

    def open_session(self, server_name: str) -> MCPSession:
        if server_name not in self.sessions:
            server = self.registry.get_server(server_name)
            session = MCPSession(server.name, server.endpoint)
            session.open()
            self.sessions[server_name] = session
            self.kernel.events.publish("mcp_session_opened", {"server": server_name})
        return self.sessions[server_name]

    def call_tool(self, server_name: str, tool_name: str, payload: Dict[str, Any] | None = None) -> Dict[str, Any]:
        session = self.open_session(server_name)
        response = session.call_tool(tool_name, payload or {})
        self.kernel.events.publish(
            "mcp_tool_called",
            {"server": server_name, "tool": tool_name, "ok": response.ok},
        )
        return {"ok": response.ok, "message": response.message, "data": response.data or {}}

    def status(self) -> Dict[str, Any]:
        return {
            "started": self.started,
            "servers": self.registry.snapshot(),
            "open_sessions": sorted(self.sessions.keys()),
        }
