# reglas.md - Estandares permanentes SkillOAF

## Proposito

Definir reglas estables que todos los agentes deben cumplir al generar software.

## Lectura obligatoria

Todo agente debe leer, en este orden:

1. `datos.md`
2. `memoria.md`
3. `reglas.md`
4. `requirements/project_requirements.yaml`
5. Skill especifico asignado

## Reglas de arquitectura

- Separar frontend, backend, database, docs, diagrams, tests y prompts.
- No mezclar responsabilidades entre capas.
- Usar nombres claros y consistentes.
- Documentar supuestos.
- Documentar pendientes.
- No inventar reglas de negocio criticas sin declararlas como supuesto.

## Reglas frontend

- Priorizar productividad operativa.
- Mantener UI clara y empresarial.
- Usar componentes reutilizables.
- Definir estados de carga, error, vacio y exito.
- No incluir SQL ni secretos.

## Reglas backend

- Separar endpoints, schemas, services, repositories y models.
- No colocar logica de negocio compleja directamente en endpoints.
- Usar variables de entorno para configuracion sensible.
- Incluir validaciones.
- Preparar auditoria y logs.

## Reglas de base de datos

- Usar claves primarias claras.
- Definir indices cuando haya busquedas frecuentes.
- Documentar relaciones.
- Preparar migracion de SQLite a PostgreSQL cuando aplique.

## Reglas de codigo Python

Todo archivo Python generado debe iniciar con encabezado:

```python
# Nombre: archivo.py
# Fecha: AAAA-MM-DD
# Utilidad: descripcion breve
# API/Funcion asociada: indicar si aplica
# Uso: ejemplo minimo
# Resultado esperado: ejemplo de salida
# Conexion API: si/no y detalle si aplica
```

## Regla de concurrencia Python

Cuando se proponga concurrencia:

- Si Python es 3.13 o inferior, ejecutar flujo normal.
- Si Python es superior a 3.13, dejar preparado flujo concurrente.

## Reglas de entrega

Todo resultado debe incluir:

- estructura de carpetas
- archivos generados
- supuestos
- pendientes
- instrucciones de ejecucion
- pruebas minimas

## Criterio ejecutivo

La salida debe permitir avanzar a desarrollo sin reuniones adicionales para reinterpretar el alcance inicial.
