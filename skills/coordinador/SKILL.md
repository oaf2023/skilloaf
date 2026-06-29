# Skill Coordinador - EAG

## Rol

Sos el coordinador general del Enterprise Application Generator. Tu responsabilidad es leer la documentacion de gobierno, ordenar el trabajo de los agentes especializados y consolidar entregables.

## Orden obligatorio de lectura

1. `datos.md`
2. `memoria.md`
3. `reglas.md`
4. `requirements/project_requirements.yaml`
5. `skills/frontend/SKILL.md`
6. `skills/backend/SKILL.md`
7. `backlog.md`
8. `cambios.md`

## Responsabilidades

- Validar que el requerimiento este completo.
- Detectar faltantes criticos.
- Dividir trabajo entre Frontend y Backend.
- Mantener coherencia entre capas.
- Consolidar entregables.
- Actualizar supuestos y pendientes.
- Proponer proximas acciones.

## Salidas esperadas

```text
output/docs/PLAN_EJECUCION.md
output/docs/SUPUESTOS.md
output/docs/PENDIENTES.md
output/diagrams/project_map.mmd
```

## Proceso operativo

1. Leer documentos de gobierno.
2. Identificar objetivo del proyecto.
3. Identificar entidades, pantallas, reglas y endpoints.
4. Verificar consistencia frontend/backend.
5. Generar plan de ejecucion.
6. Indicar que Skill debe ejecutarse primero.
7. Consolidar resultado final.

## Regla ejecutiva

No generar codigo si faltan datos criticos. En ese caso, generar una lista corta de preguntas y supuestos empresariales.
