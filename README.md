# SkillOAF - Enterprise Application Generator

Repositorio maestro para transformar requerimientos, imagenes, bocetos o documentos en especificaciones y codigo base de aplicaciones empresariales.

## Arquitectura operativa

El Skill maestro se divide en dos unidades ejecutivas:

- `skills/frontend/`: experiencia de usuario, pantallas, componentes visuales, navegacion y generacion de interfaces.
- `skills/backend/`: entidades, reglas de negocio, APIs, base de datos, seguridad, auditoria y servicios.

## Fuente de gobierno del proyecto

El agente debe leer primero:

- `datos.md`

Despues debe leer la fuente tecnica de verdad:

- `requirements/project_requirements.yaml`

## Orden de lectura del agente

1. `datos.md`
2. `requirements/project_requirements.yaml`
3. `skills/frontend/SKILL.md`
4. `skills/backend/SKILL.md`
5. `requirements/assets/`, si existen imagenes o bocetos

## Flujo recomendado

1. Completar o ajustar `datos.md` con la guia ejecutiva del trabajo.
2. Completar `requirements/project_requirements.yaml` con entidades, pantallas, reglas y criterios.
3. Adjuntar imagenes o referencias en `requirements/assets/`.
4. Ejecutar el Skill Frontend para producir pantallas, UI schema, Mermaid y codigo base.
5. Ejecutar el Skill Backend para producir modelos, API, persistencia, seguridad y pruebas.
6. Consolidar ambos entregables en una carpeta de proyecto.

## Prompt operativo corto

```text
Lee datos.md como guia operativa.
Luego lee requirements/project_requirements.yaml.
Aplica skills/frontend/SKILL.md y skills/backend/SKILL.md.
Genera los entregables en output/ manteniendo separacion entre frontend, backend, base de datos, documentacion, diagramas y pruebas.
```

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
