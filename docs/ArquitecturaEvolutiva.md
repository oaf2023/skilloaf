# ArquitecturaEvolutiva - SkillOAF Studio

## Titulo

**Arquitectura Evolutiva de SkillOAF Studio**  
Documento rector para consolidar una plataforma estable, extensible y gobernada.

## Version

RFC-0002  
Estado: Base rectora de arquitectura  
Fecha: 2026-06-29  
Autor: Oscar Fontana / SkillOAF

---

## 1. Objetivo del documento

Este documento establece las reglas estructurales para que SkillOAF Studio pueda evolucionar durante muchos anos sin comprometer su nucleo.

Define:

1. Las capas estables de SkillOAF Studio.
2. Las reglas para que ningun modulo rompa el Kernel.
3. El mecanismo formal para incorporar agentes, procesos, proveedores IA y plugins.

---

## 2. Principio rector

SkillOAF Studio debe crecer como una plataforma, no como una coleccion de scripts.

Toda nueva funcionalidad debe integrarse mediante contratos estables, buses, servicios o registros. Ningun componente debe acoplarse directamente a implementaciones internas del Kernel.

---

## 3. Capas estables

```text
SkillOAF Studio
│
├── Studio UI
├── Services
├── Runtime
├── Processes
├── Agents
├── Core / Microkernel
├── SDK
├── Providers
├── Marketplace
└── Infrastructure
```

### 3.1 Studio UI

Capa visual. En version 1.0 sera implementada con Flet.

Responsabilidades:

- mostrar proyectos
- lanzar procesos
- mostrar agentes
- mostrar artefactos
- mostrar logs y metricas
- editar procesos
- operar configuracion

Prohibiciones:

- no ejecutar reglas de negocio
- no acceder directamente al almacenamiento interno del Kernel
- no invocar proveedores IA directamente

### 3.2 Services

Capa futura de servicios estables.

Ejemplos:

- Project Service
- Agent Service
- Process Service
- Artifact Service
- Governance Service
- AI Service
- Memory Service

### 3.3 Runtime

Responsable de ejecutar procesos y tareas.

Componentes actuales:

- TaskQueue
- Dispatcher
- Scheduler
- Workflow
- StudioSession

### 3.4 Processes

Define procesos declarativos reutilizables.

Un proceso indica que agentes participan, en que orden y con que payload.

### 3.5 Agents

Agentes especialistas desacoplados.

Todos deben heredar de `BaseAgent` y registrarse mediante un registro formal.

### 3.6 Core / Microkernel

Nucleo minimo estable.

Responsabilidades:

- buses
- memoria
- artefactos
- configuracion
- logs
- metricas
- registro de agentes
- estado del sistema

### 3.7 SDK

Futura capa publica para que terceros creen extensiones sin tocar el Kernel.

### 3.8 Providers

Proveedores IA y conectores externos.

Regla: ningun agente debe invocar un proveedor directamente. Debe usar AI Manager.

### 3.9 Marketplace

Repositorio futuro de skills, agentes, procesos, plantillas, providers y plugins.

### 3.10 Infrastructure

Persistencia, archivos, entorno local, repositorios, Docker y despliegue.

---

## 4. Reglas para proteger el Kernel

### Regla 1 - El Kernel no depende de UI

El Kernel debe funcionar por CLI, API o tests sin Flet ni interfaz grafica.

### Regla 2 - El Kernel no depende de proveedores IA

OpenAI, Gemini, Claude, Ollama, LM Studio u otros deben integrarse mediante AI Manager.

### Regla 3 - Los agentes no se llaman entre si

Todo intercambio pasa por:

- Kernel
- AgentBus
- EventBus
- MemoryBus
- ArtifactEngine

### Regla 4 - Toda accion relevante genera evento

Ejemplos:

- kernel_booted
- agent_initialized
- process_started
- process_completed
- artifact_created
- validation_failed

### Regla 5 - Todo artefacto debe registrarse

No basta con crear archivos. Todo archivo producido debe registrarse en ArtifactEngine.

### Regla 6 - Toda decision debe quedar en memoria

Las decisiones tecnicas y funcionales deben almacenarse en MemoryBus o en documentos de gobierno.

### Regla 7 - Los procesos deben validarse antes de ejecutarse

Todo proceso pasa por Parser, Validator, Compiler y recien despues Runtime.

### Regla 8 - Los componentes nuevos entran por contrato

No se aceptan integraciones directas ni accesos laterales al Kernel.

---

## 5. Incorporacion de nuevos agentes

Un nuevo agente debe cumplir:

1. Heredar de `BaseAgent`.
2. Definir `name`, `role` y `version`.
3. Implementar `handle(task)`.
4. Usar ArtifactEngine para generar archivos.
5. Usar MemoryBus para decisiones, supuestos o pendientes.
6. Publicar eventos relevantes.
7. Registrarse mediante `agents/registry.py`.

Ejemplo conceptual:

```python
class SeguridadAgent(BaseAgent):
    name = "seguridad"
    role = "Evalua riesgos y controles"
    version = "0.1.0"
```

---

## 6. Incorporacion de nuevos procesos

Un nuevo proceso debe cumplir:

1. Declararse como JSON en `processes/templates/`.
2. Tener `name`, `version`, `description` y `steps`.
3. Usar agentes registrados.
4. Validarse con ProcessValidator.
5. Registrarse en `processes/catalog.py`.

---

## 7. Incorporacion de proveedores IA

Los proveedores IA entraran en version 0.5 mediante AI Manager.

Reglas:

- ningun agente consume directamente una API IA
- las claves se gestionan fuera del codigo
- el proveedor debe tener contrato comun
- el Kernel no conoce proveedores concretos

---

## 8. Incorporacion de plugins

Los plugins deberan integrarse mediante SDK y Marketplace.

Reglas:

- no modifican archivos core directamente
- no acceden a memoria interna salvo por servicios publicos
- declaran version, compatibilidad y permisos
- pueden aportar agentes, procesos, providers o templates

---

## 9. Cierre tecnico de version 0.2

La version 0.2 se considera consolidada cuando existan:

```text
core/project_manager.py
core/state_machine.py
agents/registry.py
processes/catalog.py
```

Estos modulos formalizan ciclo de vida de proyecto, estados oficiales, registro de agentes y catalogo de procesos.

---

## 10. Decision fundacional

A partir de este documento, toda expansion de SkillOAF Studio debe respetar contratos, capas y buses. El Kernel es estable, minimo y protegido. Las capacidades crecen hacia afuera mediante agentes, procesos, providers, plugins y servicios.
