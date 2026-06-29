# Nombre: asistente_proyecto.py
# Fecha: 2026-06-29
# Utilidad: asistente local para crear una carpeta de trabajo de proyecto y copiar/crear la estructura Skill Maestro.
# API/Funcion asociada: sin conexion a API externa; usa librerias estandar de Python.
# Descripcion: realiza preguntas ejecutivas, crea una carpeta local destino y genera estructura de proyecto, gobierno, requirements, skills y output.
# Uso: python tools/asistente_proyecto.py --destino "C:/Proyectos/MiProyecto" --wizard
# Resultado esperado: carpeta destino creada con datos.md, memoria.md, reglas.md, requirements, skills, output y panel HTML.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

import argparse
import html
import platform
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Tuple


ORIGEN_SKILLOAF = Path(__file__).resolve().parents[1]


@dataclass
class ProyectoConfig:
    """Configuracion ejecutiva capturada por el asistente de proyecto."""

    nombre: str
    destino: Path
    objetivo: str
    industria: str
    contexto: str
    frontend: str
    backend: str
    base_datos: str
    modo_inicial: str
    modo_futuro: str
    requiere_login: str
    requiere_reportes: str
    requiere_api: str
    modulos: str
    decisiones: str
    pendientes: str


def python_superior_313() -> bool:
    """Devuelve True si la version de Python es superior a 3.13."""
    return sys.version_info > (3, 13)


def preguntar(campo: str, default: str) -> str:
    """Pregunta un dato por consola y usa un valor por defecto si no hay respuesta."""
    valor = input(f"{campo} [{default}]: ").strip()
    return valor or default


def normalizar_nombre(nombre: str) -> str:
    """Normaliza un nombre para carpeta o identificador simple."""
    limpio = "".join(c if c.isalnum() else "_" for c in nombre.strip().lower())
    return "_".join(part for part in limpio.split("_") if part) or "nuevo_proyecto"


def ejecutar_wizard(destino_base: Path | None) -> ProyectoConfig:
    """Ejecuta entrevista ejecutiva para crear la carpeta de trabajo."""
    print("\nSkillOAF - Asistente de Proyecto")
    print("Este asistente crea una carpeta local lista para trabajar con agentes.\n")

    nombre = preguntar("Nombre del proyecto", "CRUD Clientes - Fichero Alfabetico")
    if destino_base is None:
        destino_txt = preguntar("Carpeta local destino", str(Path.cwd() / normalizar_nombre(nombre)))
        destino = Path(destino_txt).expanduser().resolve()
    else:
        destino = destino_base.expanduser().resolve()

    return ProyectoConfig(
        nombre=nombre,
        destino=destino,
        objetivo=preguntar(
            "Objetivo ejecutivo",
            "Crear una aplicacion empresarial modular apoyada por agentes.",
        ),
        industria=preguntar("Industria / area", "Gestion empresarial"),
        contexto=preguntar(
            "Contexto de negocio",
            "Sistema operativo para capturar datos, gestionar entidades, consultar informacion y generar reportes.",
        ),
        frontend=preguntar("Frontend preferido", "Flet"),
        backend=preguntar("Backend preferido", "FastAPI"),
        base_datos=preguntar("Base de datos", "SQLite inicial; PostgreSQL futuro"),
        modo_inicial=preguntar("Modo inicial", "local"),
        modo_futuro=preguntar("Modo futuro", "red multiusuario"),
        requiere_login=preguntar("Requiere login", "si"),
        requiere_reportes=preguntar("Requiere reportes", "si"),
        requiere_api=preguntar("Requiere API", "si"),
        modulos=preguntar("Modulos principales separados por coma", "Clientes, Dashboard, Reportes, Configuracion"),
        decisiones=preguntar(
            "Decisiones tomadas",
            "Separar frontend, backend, database, docs, diagrams, tests y prompts.",
        ),
        pendientes=preguntar(
            "Pendientes principales",
            "Definir entidades finales, reglas de negocio, pantallas y endpoints.",
        ),
    )


def config_por_defecto(destino: Path) -> ProyectoConfig:
    """Crea una configuracion por defecto para ejecucion no interactiva."""
    return ProyectoConfig(
        nombre="CRUD Clientes - Fichero Alfabetico",
        destino=destino.expanduser().resolve(),
        objetivo="Crear una aplicacion empresarial modular apoyada por agentes.",
        industria="Gestion empresarial",
        contexto="Sistema operativo para capturar datos, gestionar entidades, consultar informacion y generar reportes.",
        frontend="Flet",
        backend="FastAPI",
        base_datos="SQLite inicial; PostgreSQL futuro",
        modo_inicial="local",
        modo_futuro="red multiusuario",
        requiere_login="si",
        requiere_reportes="si",
        requiere_api="si",
        modulos="Clientes, Dashboard, Reportes, Configuracion",
        decisiones="Separar frontend, backend, database, docs, diagrams, tests y prompts.",
        pendientes="Definir entidades finales, reglas de negocio, pantallas y endpoints.",
    )


def crear_carpetas(destino: Path) -> None:
    """Crea estructura base de trabajo para proyecto y Skill Maestro."""
    carpetas = [
        destino / "requirements" / "assets",
        destino / "skills" / "coordinador",
        destino / "skills" / "frontend",
        destino / "skills" / "backend",
        destino / "skills" / "database",
        destino / "skills" / "qa",
        destino / "skills" / "devops",
        destino / "output" / "frontend",
        destino / "output" / "backend",
        destino / "output" / "database",
        destino / "output" / "docs",
        destino / "output" / "diagrams",
        destino / "output" / "tests",
        destino / "output" / "prompts",
        destino / "templates",
        destino / "tools",
        destino / "logs",
    ]
    for carpeta in carpetas:
        carpeta.mkdir(parents=True, exist_ok=True)


def md_datos(c: ProyectoConfig) -> str:
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""# datos.md - Guia ejecutiva del proyecto

Generado: {fecha}

## Proyecto

Nombre: {c.nombre}

Industria / area: {c.industria}

## Objetivo

{c.objetivo}

## Contexto de negocio

{c.contexto}

## Orden de lectura del agente

1. `datos.md`
2. `memoria.md`
3. `reglas.md`
4. `requirements/project_requirements.yaml`
5. `skills/coordinador/SKILL.md`
6. `skills/frontend/SKILL.md`
7. `skills/backend/SKILL.md`
8. `requirements/assets/`

## Stack ejecutivo

- Frontend: {c.frontend}
- Backend: {c.backend}
- Base de datos: {c.base_datos}
- Modo inicial: {c.modo_inicial}
- Modo futuro: {c.modo_futuro}

## Alcance operativo inicial

- Login: {c.requiere_login}
- Reportes: {c.requiere_reportes}
- API: {c.requiere_api}
- Modulos: {c.modulos}

## Regla principal

El agente debe generar entregables en `output/` sin mezclar responsabilidades entre capas.

## Prompt de ejecucion

```text
Lee datos.md, memoria.md y reglas.md.
Luego lee requirements/project_requirements.yaml.
Aplica skills/coordinador/SKILL.md, skills/frontend/SKILL.md y skills/backend/SKILL.md.
Genera la solucion en output/ con documentacion, diagramas, codigo base y pruebas.
```
"""


def md_memoria(c: ProyectoConfig) -> str:
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""# memoria.md - Decisiones del proyecto

Generado: {fecha}

## Decisiones tomadas

{c.decisiones}

## Stack definido

- Frontend: {c.frontend}
- Backend: {c.backend}
- Base de datos: {c.base_datos}

## Modelo de trabajo

El proyecto se trabajara con agentes especializados, coordinados por archivos de gobierno y por una fuente tecnica en YAML.

## Pendientes

{c.pendientes}
"""


def md_reglas(_: ProyectoConfig) -> str:
    return """# reglas.md - Reglas permanentes del proyecto

## Arquitectura

- Separar frontend, backend, database, docs, diagrams, tests y prompts.
- No mezclar SQL dentro del frontend.
- No mezclar componentes visuales dentro del backend.
- Documentar supuestos y pendientes.
- Usar nombres claros y consistentes.

## Python

Todo script Python generado debe iniciar con:

```python
# Nombre: archivo.py
# Fecha: AAAA-MM-DD
# Utilidad: descripcion breve
# API/Funcion asociada: indicar si aplica
# Uso: ejemplo minimo
# Resultado esperado: ejemplo de salida
# Conexion API: si/no y detalle si aplica
```

## Concurrencia

- Python 3.13 o inferior: flujo normal.
- Version superior a 3.13: preparar flujo concurrente cuando aporte valor.

## Entregables

Todo agente debe entregar:

- estructura de carpetas
- codigo base
- documentacion
- diagramas Mermaid
- pruebas minimas
- supuestos
- pendientes
"""


def yaml_requirements(c: ProyectoConfig) -> str:
    modulos_yaml = "\n".join(f"    - {m.strip()}" for m in c.modulos.split(",") if m.strip())
    return f"""project:
  name: "{c.nombre}"
  industry: "{c.industria}"
  objective: "{c.objetivo}"
  business_context: "{c.contexto}"

platform:
  frontend_preferred: "{c.frontend}"
  backend_preferred: "{c.backend}"
  database_preferred: "{c.base_datos}"
  mode_initial: "{c.modo_inicial}"
  mode_future: "{c.modo_futuro}"

features:
  login_required: "{c.requiere_login}"
  reports_required: "{c.requiere_reportes}"
  api_required: "{c.requiere_api}"

modules:
{modulos_yaml or '    - Modulo principal'}

acceptance_criteria:
  - "La estructura local del proyecto queda preparada para agentes."
  - "Los entregables se generan en output/."
  - "Frontend y backend quedan separados."
  - "La documentacion permite continuar sin reinterpretar el alcance."

open_questions:
  - "Definir entidades finales."
  - "Definir reglas de negocio criticas."
  - "Definir pantallas principales."
  - "Definir endpoints iniciales."
"""


def md_backlog(c: ProyectoConfig) -> str:
    return f"""# backlog.md - Trabajo pendiente

## Proyecto

{c.nombre}

## Fase 1 - Gobierno

- [x] Crear estructura local.
- [x] Crear datos.md.
- [x] Crear memoria.md.
- [x] Crear reglas.md.
- [x] Crear requirements/project_requirements.yaml.

## Fase 2 - Analisis

- [ ] Ejecutar Skill Coordinador.
- [ ] Validar entidades.
- [ ] Validar pantallas.
- [ ] Validar endpoints.

## Fase 3 - Generacion

- [ ] Generar frontend.
- [ ] Generar backend.
- [ ] Generar base de datos.
- [ ] Generar pruebas.
- [ ] Generar documentacion.
"""


def md_cambios(c: ProyectoConfig) -> str:
    fecha = datetime.now().strftime("%Y-%m-%d")
    return f"""# cambios.md - Historial

## {fecha}

- Creada estructura local para `{c.nombre}`.
- Generados archivos de gobierno.
- Generada fuente tecnica `requirements/project_requirements.yaml`.
- Preparado espacio `output/` para agentes.
"""


def md_readme(c: ProyectoConfig) -> str:
    return f"""# {c.nombre}

Proyecto creado con SkillOAF.

## Inicio operativo

```bash
python tools/asistente_proyecto.py --destino . --wizard
```

## Orden de lectura para agentes

1. datos.md
2. memoria.md
3. reglas.md
4. requirements/project_requirements.yaml
5. skills/coordinador/SKILL.md
6. skills/frontend/SKILL.md
7. skills/backend/SKILL.md

## Salida esperada

Los agentes deben generar entregables en `output/`.
"""


def skill_generico(nombre: str, foco: str) -> str:
    return f"""# Skill {nombre}

## Rol

Agente especializado en {foco}.

## Entrada obligatoria

Leer:

1. `datos.md`
2. `memoria.md`
3. `reglas.md`
4. `requirements/project_requirements.yaml`

## Salida

Generar entregables dentro de `output/` en la carpeta que corresponda.

## Regla ejecutiva

No mezclar responsabilidades con otros agentes. Documentar supuestos y pendientes.
"""


def html_panel(c: ProyectoConfig) -> str:
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datos = {
        "Proyecto": c.nombre,
        "Industria": c.industria,
        "Objetivo": c.objetivo,
        "Frontend": c.frontend,
        "Backend": c.backend,
        "Base de datos": c.base_datos,
        "Modo inicial": c.modo_inicial,
        "Modo futuro": c.modo_futuro,
        "Modulos": c.modulos,
    }
    filas = "\n".join(f"<tr><th>{html.escape(k)}</th><td>{html.escape(v)}</td></tr>" for k, v in datos.items())
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(c.nombre)} - Panel SkillOAF</title>
<style>
body {{ margin:0; font-family:Segoe UI, Arial, sans-serif; background:#f3f6fb; color:#1f2937; }}
header {{ background:#183b67; color:white; padding:30px 42px; }}
main {{ max-width:1100px; margin:28px auto; padding:0 18px; }}
.card {{ background:white; border-radius:14px; padding:24px; box-shadow:0 8px 24px rgba(0,0,0,.08); margin-bottom:20px; }}
h1 {{ margin:0; }}
th, td {{ padding:13px; border-bottom:1px solid #e5e7eb; text-align:left; vertical-align:top; }}
th {{ width:220px; background:#f9fafb; }}
table {{ width:100%; border-collapse:collapse; }}
.badge {{ display:inline-block; padding:6px 10px; border-radius:999px; background:#d1fae5; color:#065f46; font-weight:700; }}
code {{ background:#eef2ff; padding:3px 6px; border-radius:6px; }}
</style>
</head>
<body>
<header>
<h1>{html.escape(c.nombre)}</h1>
<p>Panel de gobierno generado por SkillOAF - {html.escape(fecha)}</p>
</header>
<main>
<section class="card">
<h2>Resumen ejecutivo</h2>
<p><span class="badge">Carpeta lista para agentes</span></p>
<table>{filas}</table>
</section>
<section class="card">
<h2>Orden de ejecucion</h2>
<ol>
<li><code>datos.md</code></li>
<li><code>memoria.md</code></li>
<li><code>reglas.md</code></li>
<li><code>requirements/project_requirements.yaml</code></li>
<li><code>skills/coordinador/SKILL.md</code></li>
<li><code>skills/frontend/SKILL.md</code></li>
<li><code>skills/backend/SKILL.md</code></li>
</ol>
</section>
</main>
</body>
</html>
"""


def copiar_si_existe(origen: Path, destino: Path, overwrite: bool) -> Tuple[Path, str]:
    """Copia un archivo si existe; si no existe, omite."""
    if not origen.exists():
        return destino, "origen inexistente"
    if destino.exists() and not overwrite:
        return destino, "omitido"
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(origen, destino)
    return destino, "copiado"


def escribir(path: Path, contenido: str, overwrite: bool) -> Tuple[Path, str]:
    """Escribe archivo respetando overwrite."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return path, "omitido"
    path.write_text(contenido, encoding="utf-8")
    return path, "creado/actualizado"


def generar(c: ProyectoConfig, overwrite: bool, copiar_skills_maestros: bool) -> List[Tuple[Path, str]]:
    """Genera la carpeta local con estructura de proyecto y Skill Maestro."""
    crear_carpetas(c.destino)

    archivos: List[Tuple[Path, str]] = [
        (c.destino / "README.md", md_readme(c)),
        (c.destino / "datos.md", md_datos(c)),
        (c.destino / "memoria.md", md_memoria(c)),
        (c.destino / "reglas.md", md_reglas(c)),
        (c.destino / "backlog.md", md_backlog(c)),
        (c.destino / "cambios.md", md_cambios(c)),
        (c.destino / "requirements" / "project_requirements.yaml", yaml_requirements(c)),
        (c.destino / "output" / "docs" / "panel_gobierno.html", html_panel(c)),
        (c.destino / "skills" / "database" / "SKILL.md", skill_generico("Database", "modelo de datos, SQL, migraciones e indices")),
        (c.destino / "skills" / "qa" / "SKILL.md", skill_generico("QA", "pruebas, validacion, casos limite y calidad")),
        (c.destino / "skills" / "devops" / "SKILL.md", skill_generico("DevOps", "despliegue, Docker, entorno y automatizacion")),
    ]

    resultados: List[Tuple[Path, str]] = []

    def escribir_item(item: Tuple[Path, str]) -> Tuple[Path, str]:
        return escribir(item[0], item[1], overwrite)

    if python_superior_313():
        with ThreadPoolExecutor() as executor:
            resultados.extend(executor.map(escribir_item, archivos))
    else:
        resultados.extend(escribir_item(item) for item in archivos)

    if copiar_skills_maestros:
        copias = [
            (ORIGEN_SKILLOAF / "skills" / "coordinador" / "SKILL.md", c.destino / "skills" / "coordinador" / "SKILL.md"),
            (ORIGEN_SKILLOAF / "skills" / "frontend" / "SKILL.md", c.destino / "skills" / "frontend" / "SKILL.md"),
            (ORIGEN_SKILLOAF / "skills" / "backend" / "SKILL.md", c.destino / "skills" / "backend" / "SKILL.md"),
            (ORIGEN_SKILLOAF / "tools" / "generador.py", c.destino / "tools" / "generador.py"),
            (ORIGEN_SKILLOAF / "tools" / "asistente_proyecto.py", c.destino / "tools" / "asistente_proyecto.py"),
        ]
        resultados.extend(copiar_si_existe(origen, destino, overwrite) for origen, destino in copias)

    return resultados


def imprimir_resumen(c: ProyectoConfig, resultados: Iterable[Tuple[Path, str]]) -> None:
    """Imprime resultado ejecutivo."""
    print("\nProyecto preparado")
    print(f"Destino: {c.destino}")
    print(f"Python: {platform.python_version()}")
    print(f"Modo concurrente preparado: {'si' if python_superior_313() else 'no, flujo normal'}")
    print("\nArchivos:")
    for path, estado in resultados:
        try:
            relativo = path.relative_to(c.destino)
        except ValueError:
            relativo = path
        print(f"- {relativo}: {estado}")
    print("\nSiguiente comando sugerido:")
    print(f"cd {c.destino}")
    print("Abrir output/docs/panel_gobierno.html y luego ejecutar el agente con datos.md como primer archivo.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Asistente de proyecto SkillOAF")
    parser.add_argument("--destino", help="Carpeta local donde se creara el proyecto")
    parser.add_argument("--wizard", action="store_true", help="Activa preguntas guiadas")
    parser.add_argument("--overwrite", action="store_true", help="Sobrescribe archivos existentes")
    parser.add_argument("--no-copiar-skills", action="store_true", help="No copia skills maestros desde el repositorio SkillOAF")
    args = parser.parse_args()

    destino = Path(args.destino).expanduser().resolve() if args.destino else None

    if args.wizard:
        config = ejecutar_wizard(destino)
    else:
        if destino is None:
            destino = Path.cwd() / "nuevo_proyecto_skilloaf"
        config = config_por_defecto(destino)

    resultados = generar(config, overwrite=args.overwrite, copiar_skills_maestros=not args.no_copiar_skills)
    imprimir_resumen(config, resultados)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
