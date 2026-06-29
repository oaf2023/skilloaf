# PlanGral - SkillOAF Studio

## Titulo

**SkillOAF Studio: Un Sistema Operativo para Ingenieria de Software asistida por IA**

## Version

RFC-0001  
Estado: Borrador fundacional  
Fecha: 2026-06-29  
Autor: Oscar Fontana / SkillOAF

---

## 1. Vision

SkillOAF Studio nace como una plataforma para convertir ideas, requerimientos, imagenes, documentos y reglas de negocio en proyectos de software completos, gobernados por agentes especializados.

No se define solamente como un generador de codigo. Se define como un **Sistema Operativo para Ingenieria de Software asistida por IA**, donde cada agente funciona como un proceso especializado conectado a un nucleo comun.

El objetivo es transformar el desarrollo de software en una fabrica organizada, auditable, repetible y escalable.

---

## 2. Principio rector

SkillOAF Studio no debe limitarse a responder preguntas.

Debe producir artefactos:

- requerimientos
- arquitectura
- diagramas
- prompts
- frontend
- backend
- base de datos
- documentacion
- pruebas
- despliegue
- bitacora de decisiones

La respuesta conversacional es secundaria. El valor central es el artefacto generado.

---

## 3. Diferencia frente a un IDE tradicional

Un IDE tradicional ayuda a programar.

SkillOAF Studio debe ayudar a **construir software completo con agentes**.

Diferencias principales:

| Herramienta tradicional | SkillOAF Studio |
|---|---|
| Editor de codigo | Sistema de agentes |
| Archivos sueltos | Artefactos gobernados |
| Programador ejecuta | Agentes colaboran |
| Memoria limitada | Memoria del proyecto |
| Generacion puntual | Flujo completo de ingenieria |
| Proyecto manual | Proyecto asistido y auditable |

---

## 4. Arquitectura conceptual tipo microkernel

SkillOAF Studio se organiza como un microkernel.

```text
SkillOAF Studio

                 Kernel
                    │
     ┌──────────────┼──────────────┐
     │              │              │
 Agent Bus      Event Bus      Memory Bus
     │              │              │
 ┌───┴────┐    ┌────┴────┐    ┌────┴────┐
 │        │    │         │    │         │
Frontend Backend Database  QA DevOps  UX Seguridad Documentador
```

### Kernel

El Kernel coordina estado, reglas, eventos, memoria, agentes y artefactos.

### Agent Bus

Canal por el cual los agentes reciben tareas, entregan resultados y solicitan informacion.

### Event Bus

Canal de eventos del sistema:

- proyecto_creado
- requerimiento_actualizado
- frontend_generado
- backend_generado
- schema_modificado
- prueba_fallida
- deploy_preparado

### Memory Bus

Canal de lectura y escritura de memoria:

- memoria del proyecto
- decisiones
- restricciones
- preferencias tecnicas
- historico de cambios
- supuestos

---

## 5. Componentes principales

```text
SkillOAF Studio
│
├── Kernel
├── Project Manager
├── Agent Manager
├── Memory Manager
├── Prompt Engine
├── Template Engine
├── Artifact Engine
├── Validation Engine
├── Documentation Engine
├── Test Engine
├── Plugin Engine
└── Studio UI
```

### Project Manager

Crea, abre, versiona y administra proyectos.

### Agent Manager

Registra agentes, roles, habilidades, entradas y salidas.

### Memory Manager

Administra memoria funcional, tecnica, historica y ejecutiva.

### Prompt Engine

Construye prompts consistentes a partir de reglas, memoria y requerimientos.

### Template Engine

Genera codigo, documentos y estructuras desde plantillas.

### Artifact Engine

Administra los artefactos producidos por agentes.

### Validation Engine

Verifica consistencia entre frontend, backend, database, tests y documentacion.

### Plugin Engine

Permite incorporar nuevos especialistas, frameworks, conectores y plantillas.

### Studio UI

Interfaz visual tipo IDE para operar proyectos, agentes y artefactos.

---

## 6. Sistema de gobierno documental

Cada proyecto debe tener archivos de gobierno.

```text
Proyecto/
│
├── datos.md
├── memoria.md
├── reglas.md
├── backlog.md
├── cambios.md
├── requirements/
│   └── project_requirements.yaml
└── skills/
```

### datos.md

Tablero ejecutivo del proyecto.

### memoria.md

Decisiones tomadas y criterios que no deben reabrirse sin motivo.

### reglas.md

Normas permanentes de arquitectura, codigo, documentacion y entrega.

### backlog.md

Pendientes y fases futuras.

### cambios.md

Historial del proyecto.

### project_requirements.yaml

Fuente tecnica de verdad.

---

## 7. Memoria del proyecto

SkillOAF Studio debe tener memoria del proyecto, no solamente memoria del usuario.

Ejemplo:

```text
Proyecto ERP Taller

Recuerda:
- usar Flet
- usar FastAPI
- SQLite en prototipo
- PostgreSQL en produccion
- evitar Tkinter
- documentar en espanol
- preparar compatibilidad Python 3.13
- generar diagramas Mermaid
```

La memoria del proyecto evita contradicciones, cambios arbitrarios y perdida de contexto.

---

## 8. Agentes especialistas

Los agentes representan roles reales de un equipo de software.

Agentes iniciales:

- Coordinador
- Analista Funcional
- Arquitecto
- UX/UI
- Frontend
- Backend
- Database
- QA
- DevOps
- Seguridad
- Documentador
- Integraciones
- IA

Cada agente debe tener:

- rol
- responsabilidades
- entradas
- salidas
- restricciones
- criterios de calidad
- carpeta de trabajo

---

## 9. Artefactos

SkillOAF Studio trabaja con artefactos versionables.

Tipos de artefactos:

```text
output/
├── frontend/
├── backend/
├── database/
├── docs/
├── diagrams/
├── prompts/
├── tests/
├── deploy/
└── logs/
```

Cada artefacto debe poder ser revisado, regenerado, auditado y mejorado.

---

## 10. Flujo operativo principal

```text
Idea
  │
  ▼
Asistente de Proyecto
  │
  ▼
Gobierno documental
  │
  ▼
Skill Coordinador
  │
  ├── Frontend Agent
  ├── Backend Agent
  ├── Database Agent
  ├── QA Agent
  ├── DevOps Agent
  └── Documentador
  │
  ▼
Artefactos versionados
  │
  ▼
Proyecto ejecutable
```

---

## 11. SkillOAF Studio como producto

SkillOAF Studio debe evolucionar en tres capas.

### Capa 1 - CLI

Scripts locales para crear estructura, gobierno, requerimientos y artefactos.

### Capa 2 - Studio UI

Aplicacion visual para administrar proyectos, agentes, prompts, artefactos y logs.

### Capa 3 - Plataforma multiagente

Kernel, buses, plugins, templates y proveedores IA intercambiables.

---

## 12. Relacion con Google AI Studio

Google AI Studio se orienta a crear, probar y operar prompts/modelos.

SkillOAF Studio se inspira en esa experiencia, pero se enfoca en ingenieria de software empresarial:

- proyectos completos
- agentes especialistas
- memoria del proyecto
- artefactos versionables
- reglas de arquitectura
- generacion de frontend/backend/database/docs/tests

---

## 13. Roadmap

### Version 0.1 - Base operativa

- Repositorio SkillOAF
- datos.md
- memoria.md
- reglas.md
- project_requirements.yaml
- Skill Coordinador
- Skill Frontend
- Skill Backend
- tools/generador.py
- tools/asistente_proyecto.py

### Version 0.2 - Gobierno extendido

- Skill Database
- Skill QA
- Skill DevOps
- Skill Documentador
- Panel HTML del proyecto
- Validacion basica de estructura

### Version 0.5 - Generador real

- Template Engine inicial
- Generacion Flet
- Generacion FastAPI
- Generacion SQLite/PostgreSQL
- Generacion Mermaid
- Generacion README/API/TESTS

### Version 1.0 - SkillOAF Studio Desktop

- UI en Flet
- Gestor de proyectos
- Editor de requerimientos
- Consola de agentes
- Visor de artefactos
- Panel de estado
- Ejecucion asistida de agentes

### Version 2.0 - Plataforma multiagente

- Kernel
- Agent Bus
- Event Bus
- Memory Bus
- Marketplace de Skills
- Plugins
- Integracion con proveedores IA

---

## 14. Proveedores IA futuros

SkillOAF Studio debe poder integrarse con diferentes proveedores:

- OpenAI
- Gemini
- Claude
- Ollama
- LM Studio
- OpenRouter
- Azure OpenAI
- modelos locales
- MCP

El proveedor IA no debe estar acoplado al nucleo.

---

## 15. Marketplace de Skills

A futuro se podran incorporar Skills por dominio:

- CRM
- ERP
- Odontologia
- Stock
- Mantenimiento
- RFID
- GPS
- Ventas
- POS
- Snowflake
- SQLite
- PostgreSQL
- MercadoPago
- AFIP / ARCA
- Telegram
- WhatsApp

---

## 16. Criterios de calidad

Todo resultado generado por SkillOAF Studio debe cumplir:

- trazabilidad
- modularidad
- documentacion
- separacion de responsabilidades
- versionabilidad
- reproducibilidad
- pruebas minimas
- claridad empresarial
- compatibilidad evolutiva

---

## 17. Decision fundacional

SkillOAF Studio sera desarrollado como una plataforma de ingenieria asistida por IA bajo arquitectura de microkernel, donde los agentes son especialistas desacoplados que producen artefactos sobre una memoria de proyecto compartida.

Esta decision guia todo el desarrollo futuro.

---

## 18. Proxima accion

Crear los siguientes componentes:

```text
core/
├── kernel.py
├── agent_bus.py
├── event_bus.py
├── memory_bus.py
└── artifact_engine.py
```

Y luego crear una primera interfaz:

```text
studio/
└── app.py
```

con Flet, para administrar proyectos y ejecutar el asistente local.
