# Nombre: client.py
# Fecha: 2026-06-29
# Utilidad: cliente MCP placeholder para SkillOAF Studio.
# API/Funcion asociada: MCPClient.connect / call_tool.
# Descripcion: define contrato inicial para comunicarse con servidores MCP sin acoplar el Kernel.
# Uso: client = MCPClient('stdio://github'); client.connect(); client.call_tool('search', {'q':'demo'})
# Resultado esperado: estructura de respuesta estandarizada; implementacion real pendiente.
# Conexion API: preparado para conectar a servidores MCP; no implementa transporte real todavia.

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class MCPResponse:
    ok: bool
    message: str
    data: Dict[str, Any] | None = None


class MCPClient:
    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
        self.connected = False

    def connect(self) -> MCPResponse:
        self.connected = True
        return MCPResponse(ok=True, message=f"Conexion MCP simulada: {self.endpoint}", data={"endpoint": self.endpoint})

    def disconnect(self) -> MCPResponse:
        self.connected = False
        return MCPResponse(ok=True, message="Conexion MCP cerrada", data={})

    def call_tool(self, tool_name: str, payload: Dict[str, Any] | None = None) -> MCPResponse:
        if not self.connected:
            return MCPResponse(ok=False, message="Cliente MCP no conectado", data={})
        return MCPResponse(
            ok=True,
            message=f"Tool MCP simulado ejecutado: {tool_name}",
            data={"tool": tool_name, "payload": payload or {}},
        )
