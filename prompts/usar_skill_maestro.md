# Prompt para usar SkillOAF

Copiar y pegar este prompt en el agente que vaya a trabajar el proyecto.

```text
Actua como Enterprise Application Generator.

Usa el repositorio SkillOAF como fuente de instrucciones.

Orden de ejecucion:
1. Lee requirements/project_requirements.yaml.
2. Ejecuta conceptualmente skills/frontend/SKILL.md.
3. Ejecuta conceptualmente skills/backend/SKILL.md.
4. Genera los entregables en output/.

Reglas:
- Mantener separacion entre frontend y backend.
- No mezclar SQL en la interfaz.
- No mezclar componentes visuales en el backend.
- Documentar supuestos.
- Generar Mermaid para frontend y backend.
- Generar codigo base Python con encabezado empresarial.
- Preparar SQLite para prototipo y PostgreSQL para produccion si aplica.

Entregables minimos:
- output/frontend/README_FRONTEND.md
- output/frontend/ui_schema.yaml
- output/frontend/app_frontend.py
- output/backend/README_BACKEND.md
- output/backend/app/main.py
- output/database/schema.sql
- output/docs/API.md
- output/diagrams/frontend_layout.mmd
- output/diagrams/backend_architecture.mmd
```
