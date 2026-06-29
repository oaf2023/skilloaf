# Prueba Basica - SkillOAF Studio

## Objetivo

Validar que la base minima de SkillOAF Studio funciona correctamente:

- Kernel
- Servicios
- Runtime
- Agentes
- Procesos
- Artefactos
- MCP placeholder

## Comando

Ejecutar desde la raiz del repositorio:

```bash
python tests/test_basico.py
```

## Resultado esperado

```text
OK - prueba basica completada
Proyecto temporal: .../tmp_test_project
```

## Que valida

1. El Kernel inicia.
2. Se registran los servicios fundacionales:
   - project
   - agent
   - process
   - artifact
   - knowledge
   - mcp
3. El workflow base ejecuta seis agentes:
   - coordinador
   - frontend
   - backend
   - database
   - qa
   - devops
4. Se generan artefactos en output/.
5. MCPService registra un servidor demo.
6. MCPService ejecuta una tool simulada.
7. El estado final queda en `project_loaded`.
8. Las metricas registran ejecucion de agentes.

## Nota sobre MCP

La prueba no conecta a un servidor MCP real. Usa el cliente placeholder definido en:

```text
providers/mcp/client.py
```

El objetivo de esta etapa es validar arquitectura, contrato y flujo:

```text
Kernel -> ServiceManager -> MCPService -> MCPSession -> MCPClient
```
