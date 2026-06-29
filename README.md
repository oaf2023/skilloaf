# SkillOAF - Enterprise Application Generator

Repositorio maestro para transformar requerimientos, imagenes, bocetos o documentos en especificaciones y codigo base de aplicaciones empresariales.

## Arquitectura operativa

El Skill maestro se divide en dos unidades ejecutivas:

- `skills/frontend/`: experiencia de usuario, pantallas, componentes visuales, navegacion y generacion de interfaces.
- `skills/backend/`: entidades, reglas de negocio, APIs, base de datos, seguridad, auditoria y servicios.

Ambos trabajan sobre una unica fuente de verdad:

- `requirements/project_requirements.yaml`

## Flujo recomendado

1. Completar `requirements/project_requirements.yaml`.
2. Adjuntar imagenes o referencias en `requirements/assets/`.
3. Ejecutar el Skill Frontend para producir pantallas, UI schema, Mermaid y codigo base.
4. Ejecutar el Skill Backend para producir modelos, API, persistencia, seguridad y pruebas.
5. Consolidar ambos entregables en una carpeta de proyecto.

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
