# Nombre: generador.py
# Fecha: 2026-06-29
# Utilidad: asistente local para crear archivos de gobierno del generador SkillOAF.
# API/Funcion asociada: sin conexion a API externa; usa solo librerias estandar de Python.
# Descripcion: realiza preguntas por consola y genera datos.md, memoria.md, reglas.md y un HTML estatico de carga ejecutiva.
# Uso: python tools/generador.py --wizard
# Resultado esperado: archivos datos.md, memoria.md, reglas.md y output/panel_gobierno.html creados o actualizados.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

import argparse
import html
import platform
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output"


@dataclass
class ProyectoGobierno:
    """Datos ejecutivos basicos para crear la documentacion de gobierno."""

    nombre: str
    objetivo: str
    contexto: str
    frontend: str
    backend: str
    base_datos: str
    sistema_objetivo: str
    modo_inicial: str
    modo_futuro: str
    prioridad_actual: str
    decisiones: str
    pendientes: str


def python_superior_313() -> bool:
    """Indica si la version de Python es superior a 3.13."""
    return sys.version_info > (3, 13)


def preguntar(campo: str, default: str) -> str:
    """Pregunta un dato por consola y devuelve el valor ingresado o el valor por defecto."""
    respuesta = input(f"{campo} [{default}]: ").strip()
    return respuesta or default


def ejecutar_wizard() -> ProyectoGobierno:
    """Ejecuta preguntas guiadas para construir los documentos de gobierno."""
    print("\nSkillOAF - Generador de gobierno del proyecto")
    print("Responda las preguntas. ENTER conserva el valor sugerido.\n")

    return ProyectoGobierno(
        nombre=preguntar("Nombre del proyecto", "CRUD Clientes - Fichero Alfabetico"),
        objetivo=preguntar(
            "Objetivo ejecutivo",
            "Crear una aplicacion empresarial para administrar clientes como fichas ordenadas alfabeticamente.",
        ),
        contexto=preguntar(
            "Contexto de negocio",
            "Gestion operativa de clientes con busqueda rapida, filtros, alta, modificacion, consulta y baja controlada.",
        ),
        frontend=preguntar("Frontend preferido", "Flet"),
        backend=preguntar("Backend preferido", "FastAPI"),
        base_datos=preguntar("Base de datos inicial", "SQLite; futura PostgreSQL"),
        sistema_objetivo=preguntar("Sistema objetivo", "Windows 11 y Linux"),
        modo_inicial=preguntar("Modo inicial", "local"),
        modo_futuro=preguntar("Modo futuro", "red multiusuario"),
        prioridad_actual=preguntar(
            "Prioridad actual",
            "Generar especificacion frontend, backend, base de datos, documentacion, diagramas y pruebas.",
        ),
        decisiones=preguntar(
            "Decisiones tomadas",
            "SkillOAF sera un generador de software apoyado por agentes con separacion frontend/backend.",
        ),
        pendientes=preguntar(
            "Pendientes principales",
            "Definir CLI completa, motor de templates, agentes especializados y formato maestro .eag.",
        ),
    )


def plantilla_datos(p: ProyectoGobierno) -> str:
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""# datos.md - Guia operativa local del SkillOAF

## Funcion del archivo

Este archivo es el tablero ejecutivo del agente. Debe leerse antes de cualquier Skill, plantilla o requerimiento tecnico.

Generado automaticamente: {fecha}

## Orden obligatorio de lectura

1. `datos.md`
2. `memoria.md`
3. `reglas.md`
4. `requirements/project_requirements.yaml`
5. `skills/coordinador/SKILL.md`
6. `skills/frontend/SKILL.md`
7. `skills/backend/SKILL.md`
8. Archivos complementarios dentro de `requirements/assets/`

## Proyecto actual

Nombre: {p.nombre}

Objetivo: {p.objetivo}

Contexto: {p.contexto}

## Vision funcional

La aplicacion debe responder a un flujo empresarial claro:

- entrada de requerimientos
- analisis por agentes
- generacion de estructura
- generacion de codigo base
- generacion de documentacion
- generacion de pruebas
- preparacion para despliegue

## Prioridad de ejecucion

{p.prioridad_actual}

## Stack recomendado

Frontend: {p.frontend}.
Backend: {p.backend}.
Base de datos: {p.base_datos}.
Sistema operativo objetivo: {p.sistema_objetivo}.
Modo inicial: {p.modo_inicial}.
Modo futuro: {p.modo_futuro}.

## Reglas de gobierno

- Mantener separacion estricta entre frontend y backend.
- No colocar SQL dentro del frontend.
- No colocar logica visual dentro del backend.
- Toda regla de negocio debe quedar documentada.
- Todo endpoint debe tener proposito claro.
- Toda entidad debe tener campos, tipos y validaciones.
- Toda pantalla debe tener objetivo funcional.
- Todo supuesto debe quedar declarado.
- Todo pendiente debe quedar registrado.

## Prompt corto para ejecutar el proyecto

```text
Lee datos.md como guia operativa.
Luego lee memoria.md y reglas.md.
Despues lee requirements/project_requirements.yaml.
Aplica skills/coordinador/SKILL.md, skills/frontend/SKILL.md y skills/backend/SKILL.md.
Genera los entregables en output/ manteniendo separacion empresarial.
```

## Estado actual

Estado: gobierno de proyecto generado por tools/generador.py.
Proxima accion: ejecutar el Skill Coordinador para validar alcance y plan de trabajo.
"""


def plantilla_memoria(p: ProyectoGobierno) -> str:
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""# memoria.md - Decisiones tomadas

## Proposito

Registrar decisiones estrategicas y tecnicas para que los agentes no redefinan criterios ya acordados.

Generado automaticamente: {fecha}

## Decisiones vigentes

### 1. Proyecto activo

{p.nombre}

### 2. Objetivo ejecutivo

{p.objetivo}

### 3. Decision principal

{p.decisiones}

### 4. Separacion arquitectonica

El sistema mantiene separacion entre:

- Frontend
- Backend
- Database
- Docs
- Diagrams
- Tests
- Prompts

### 5. Stack elegido

- Frontend: {p.frontend}
- Backend: {p.backend}
- Base de datos: {p.base_datos}
- Sistema objetivo: {p.sistema_objetivo}

### 6. Modelo de ejecucion

- Modo inicial: {p.modo_inicial}
- Modo futuro: {p.modo_futuro}

## Pendiente de decision

{p.pendientes}
"""


def plantilla_reglas(_: ProyectoGobierno) -> str:
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""# reglas.md - Estandares permanentes SkillOAF

## Proposito

Definir reglas estables que todos los agentes deben cumplir al generar software.

Generado automaticamente: {fecha}

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
"""


def plantilla_html(p: ProyectoGobierno) -> str:
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    campos = {
        "Proyecto": p.nombre,
        "Objetivo": p.objetivo,
        "Contexto": p.contexto,
        "Frontend": p.frontend,
        "Backend": p.backend,
        "Base de datos": p.base_datos,
        "Sistema objetivo": p.sistema_objetivo,
        "Modo inicial": p.modo_inicial,
        "Modo futuro": p.modo_futuro,
        "Prioridad": p.prioridad_actual,
        "Decisiones": p.decisiones,
        "Pendientes": p.pendientes,
    }
    filas = "\n".join(
        f"<tr><th>{html.escape(k)}</th><td>{html.escape(v)}</td></tr>" for k, v in campos.items()
    )
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SkillOAF - Panel de Gobierno</title>
  <style>
    body {{ font-family: Segoe UI, Arial, sans-serif; background:#f4f7fb; margin:0; color:#1f2937; }}
    header {{ background:#183b67; color:white; padding:28px 36px; }}
    main {{ max-width:1100px; margin:28px auto; padding:0 18px; }}
    .card {{ background:white; border-radius:14px; box-shadow:0 8px 24px rgba(0,0,0,.08); padding:24px; margin-bottom:18px; }}
    h1 {{ margin:0; font-size:30px; }}
    h2 {{ color:#183b67; }}
    table {{ width:100%; border-collapse:collapse; }}
    th, td {{ padding:14px; border-bottom:1px solid #e5e7eb; text-align:left; vertical-align:top; }}
    th {{ width:230px; color:#374151; background:#f9fafb; }}
    code {{ background:#eef2ff; padding:3px 6px; border-radius:6px; }}
    .badge {{ display:inline-block; background:#d1fae5; color:#065f46; padding:6px 10px; border-radius:999px; font-weight:600; }}
  </style>
</head>
<body>
  <header>
    <h1>SkillOAF - Panel de Gobierno</h1>
    <p>Generado automaticamente: {html.escape(fecha)}</p>
  </header>
  <main>
    <section class="card">
      <h2>Resumen ejecutivo</h2>
      <p><span class="badge">Listo para agentes</span></p>
      <table>
        {filas}
      </table>
    </section>
    <section class="card">
      <h2>Orden de lectura recomendado</h2>
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


def escribir_archivo(path: Path, contenido: str, overwrite: bool) -> Tuple[Path, str]:
    """Escribe un archivo respetando la politica de sobrescritura."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return path, "omitido"
    path.write_text(contenido, encoding="utf-8")
    return path, "creado/actualizado"


def generar_archivos(p: ProyectoGobierno, overwrite: bool) -> List[Tuple[Path, str]]:
    """Genera archivos de gobierno y panel HTML."""
    tareas: List[Tuple[Path, str]] = [
        (ROOT / "datos.md", plantilla_datos(p)),
        (ROOT / "memoria.md", plantilla_memoria(p)),
        (ROOT / "reglas.md", plantilla_reglas(p)),
        (OUTPUT_DIR / "panel_gobierno.html", plantilla_html(p)),
    ]

    if python_superior_313():
        with ThreadPoolExecutor() as executor:
            return list(executor.map(lambda item: escribir_archivo(item[0], item[1], overwrite), tareas))

    return [escribir_archivo(path, contenido, overwrite) for path, contenido in tareas]


def crear_estructura_base() -> None:
    """Crea carpetas base del generador."""
    carpetas = [
        OUTPUT_DIR / "frontend",
        OUTPUT_DIR / "backend",
        OUTPUT_DIR / "database",
        OUTPUT_DIR / "docs",
        OUTPUT_DIR / "diagrams",
        OUTPUT_DIR / "tests",
        OUTPUT_DIR / "prompts",
        ROOT / "requirements" / "assets",
        ROOT / "skills" / "frontend",
        ROOT / "skills" / "backend",
        ROOT / "skills" / "coordinador",
        ROOT / "tools",
    ]
    for carpeta in carpetas:
        carpeta.mkdir(parents=True, exist_ok=True)


def resumen(resultados: Iterable[Tuple[Path, str]]) -> None:
    """Imprime resumen operativo."""
    print("\nResumen de generacion")
    print(f"Python: {platform.python_version()}")
    print(f"Modo concurrente preparado: {'si' if python_superior_313() else 'no, flujo normal'}")
    for path, estado in resultados:
        print(f"- {path.relative_to(ROOT)}: {estado}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generador local de gobierno SkillOAF")
    parser.add_argument("--wizard", action="store_true", help="Ejecuta preguntas por consola")
    parser.add_argument("--overwrite", action="store_true", help="Sobrescribe archivos existentes")
    args = parser.parse_args()

    crear_estructura_base()

    if args.wizard:
        proyecto = ejecutar_wizard()
    else:
        proyecto = ProyectoGobierno(
            nombre="CRUD Clientes - Fichero Alfabetico",
            objetivo="Crear una aplicacion empresarial para administrar clientes como fichas ordenadas alfabeticamente.",
            contexto="Gestion operativa de clientes con busqueda rapida, filtros, alta, modificacion, consulta y baja controlada.",
            frontend="Flet",
            backend="FastAPI",
            base_datos="SQLite; futura PostgreSQL",
            sistema_objetivo="Windows 11 y Linux",
            modo_inicial="local",
            modo_futuro="red multiusuario",
            prioridad_actual="Generar especificacion frontend, backend, base de datos, documentacion, diagramas y pruebas.",
            decisiones="SkillOAF sera un generador de software apoyado por agentes con separacion frontend/backend.",
            pendientes="Definir CLI completa, motor de templates, agentes especializados y formato maestro .eag.",
        )

    resultados = generar_archivos(proyecto, overwrite=args.overwrite)
    resumen(resultados)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
