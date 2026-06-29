# datos.md - Guia operativa local del SkillOAF

## Funcion del archivo

Este archivo es el tablero ejecutivo del agente. Debe leerse antes de cualquier Skill, plantilla o requerimiento tecnico.

Define el foco de trabajo, el orden de ejecucion, las reglas de gobierno del proyecto y el estado operativo.

## Orden obligatorio de lectura

1. `datos.md`
2. `requirements/project_requirements.yaml`
3. `skills/frontend/SKILL.md`
4. `skills/backend/SKILL.md`
5. Archivos complementarios dentro de `requirements/assets/`

## Proyecto actual

Nombre: CRUD Clientes - Fichero Alfabetico

Objetivo: crear una aplicacion empresarial para administrar clientes mediante fichas visuales ordenadas alfabeticamente, con busqueda rapida, filtros, alta, modificacion, consulta y baja controlada.

## Vision funcional

La aplicacion debe comportarse como un fichero moderno:

- clientes ordenados por apellido o razon social
- indice alfabetico visible
- fichas tipo tarjeta
- busqueda global
- filtros por estado
- acciones Ver, Editar y Eliminar
- paginacion
- exportacion futura

## Prioridad de ejecucion

Fase 1: generar especificacion frontend.
Fase 2: generar especificacion backend.
Fase 3: generar base de datos.
Fase 4: integrar frontend y backend.
Fase 5: documentar instalacion, pruebas y despliegue.

## Stack recomendado

Frontend: Flet con Python.
Backend: FastAPI con Python.
Base inicial: SQLite.
Base futura: PostgreSQL.
Sistema operativo objetivo: Windows 11 y Linux.
Modo inicial: local.
Modo futuro: red multiusuario.

## Reglas de gobierno

- Mantener separacion estricta entre frontend y backend.
- No colocar SQL dentro del frontend.
- No colocar logica visual dentro del backend.
- Toda regla de negocio debe quedar documentada.
- Todo endpoint debe tener proposito claro.
- Toda entidad debe tener campos, tipos y validaciones.
- Toda pantalla debe tener objetivo funcional.
- Todo supuesto debe quedar declarado.
- Todo pendiente debe quedar en una seccion de pendientes.

## Reglas para scripts Python

Todo script Python generado debe iniciar con encabezado que indique:

- nombre del archivo
- fecha
- utilidad
- API o funcion asociada, si aplica
- descripcion breve de uso
- ejemplo minimo de uso
- ejemplo de resultado o devolucion
- aclaracion de conexion a API si corresponde

Cuando se proponga concurrencia, agregar bandera de version:

- Python 3.13 o inferior: ejecutar flujo normal.
- Version superior a 3.13: dejar preparado flujo concurrente.

## Entregables esperados

```text
output/
├── frontend/
├── backend/
├── database/
├── docs/
├── diagrams/
├── tests/
└── prompts/
```

## Criterio de aceptacion ejecutivo

El agente debe entregar una estructura que permita iniciar desarrollo sin reinterpretar la idea original.

El resultado debe ser claro, modular, mantenible y preparado para crecimiento empresarial.

## Prompt corto para ejecutar el proyecto

```text
Lee datos.md como guia operativa.
Luego lee requirements/project_requirements.yaml.
Aplica skills/frontend/SKILL.md y skills/backend/SKILL.md.
Genera los entregables en output/ manteniendo separacion empresarial entre frontend, backend, base de datos, documentacion, diagramas y pruebas.
```

## Estado actual

Estado: base del Skill maestro creada.
Proxima accion: generar primera version operativa del proyecto CRUD Clientes tipo fichero.
