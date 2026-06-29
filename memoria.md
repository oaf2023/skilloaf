# memoria.md - Decisiones tomadas

## Proposito

Registrar decisiones estrategicas y tecnicas para que los agentes no redefinan criterios ya acordados.

## Decisiones vigentes

### 1. SkillOAF sera un generador de software apoyado por agentes

El repositorio no sera solo documentacion. Debe evolucionar hacia una plataforma que convierta requerimientos en estructura, codigo base, documentacion, diagramas y pruebas.

### 2. Separacion principal

El sistema se divide en dos Skills iniciales:

- Frontend
- Backend

Ambos son coordinados por documentos de gobierno del proyecto.

### 3. Fuente ejecutiva inicial

El primer archivo que debe leer cualquier agente es:

```text
datos.md
```

### 4. Fuente tecnica

La fuente tecnica de verdad es:

```text
requirements/project_requirements.yaml
```

### 5. Stack inicial preferido

- Frontend: Flet con Python
- Backend: FastAPI con Python
- Base prototipo: SQLite
- Base produccion: PostgreSQL

### 6. Primer caso de uso

CRUD de Clientes con vista de fichero alfabetico.

### 7. Criterio empresarial

Todo entregable debe ser modular, mantenible, documentado y preparado para escalar.

## Pendiente de decision

- Definir si el generador tendra CLI propia.
- Definir si los outputs se generaran en el mismo repositorio o en repositorios independientes.
- Definir formato final del archivo maestro: YAML, JSON o formato propio `.eag`.
