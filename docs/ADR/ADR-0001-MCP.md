# ADR-0001 - MCP como canal preferente de integracion

## Estado

Aceptado para arquitectura evolutiva.

## Fecha

2026-06-29

## Contexto

SkillOAF Studio evoluciona hacia una plataforma orientada a servicios, donde el Kernel coordina, los servicios administran capacidades permanentes y los agentes ejecutan tareas concretas.

Para comunicarse con sistemas externos se requiere una capa desacoplada que permita integrar herramientas, datos, repositorios, proveedores IA, bases de datos y servicios empresariales sin modificar el Kernel.

## Decision

MCP sera tratado como canal preferente de integracion cuando exista un servidor MCP disponible.

Toda comunicacion externa debera pasar por una capa de conectores o servicios. Ningun agente debe conectarse directamente a un sistema externo.

## Regla principal

```text
Agente -> Servicio -> Conector -> MCP / API / Sistema externo
```

## Implicancias

- El Kernel no conoce detalles de MCP.
- Los agentes no invocan MCP directamente.
- MCP se integra mediante `MCPService` y `providers/mcp/`.
- Los conectores no deben romper los contratos internos.
- Cuando no exista MCP, se podra usar un conector alternativo con el mismo contrato.

## Capas previstas

```text
services/
└── mcp_service.py

providers/
└── mcp/
    ├── __init__.py
    ├── client.py
    ├── registry.py
    ├── capabilities.py
    └── session.py
```

## Resultado esperado

SkillOAF Studio podra incorporar integraciones externas sin redisenar el Kernel, priorizando MCP como mecanismo estandarizado cuando este disponible.
