# Nombre: session.py
# Fecha: 2026-06-29
# Utilidad: sesion MCP para SkillOAF Studio.
# API/Funcion asociada: MCPSession.open / call_tool / close.
# Descripcion: administra un cliente MCP asociado a un servidor registrado.
# Uso: session = MCPSession('github', 'stdio://github'); session.open(); session.call_tool('search', {'q':'demo'})
# Resultado esperado: llamadas MCP simuladas con contrato uniforme.
# Conexion API: preparado para conectar a MCP; transporte real pendiente.

from __future__ import annotations

from typing import Any, Dict

from providers.mcp.client import MCPClient, MCPResponse


class MCPSession:
    def __init__(self, server_name: str, endpoint: str) -> None:
        self.server_name = server_name
        self.client = MCPClient(endpoint)

    def open(self) -> MCPResponse:
        return self.client.connect()

    def close(self) -> MCPResponse:
        return self.client.disconnect()

    def call_tool(self, tool_name: str, payload: Dict[str, Any] | None = None) -> MCPResponse:
        return self.client.call_tool(tool_name, payload or {})
