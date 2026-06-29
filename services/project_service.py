# Nombre: project_service.py
# Fecha: 2026-06-29
# Utilidad: servicio permanente de gestion de proyectos en SkillOAF Studio.
# API/Funcion asociada: ProjectService.open / status.
# Descripcion: encapsula ProjectManager para que el Kernel no gestione directamente detalles de proyecto.
# Uso: service = ProjectService(kernel); service.start(); service.open()
# Resultado esperado: proyecto abierto y metadatos disponibles.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Any, Dict


class ProjectService:
    name = "project"

    def __init__(self, kernel: Any) -> None:
        self.kernel = kernel
        self.started = False

    def start(self) -> None:
        self.started = True

    def stop(self) -> None:
        self.started = False

    def open(self) -> Dict[str, Any]:
        metadata = self.kernel.project.open_project()
        self.kernel.memory.set("project.name", metadata.name)
        self.kernel.memory.set("project.root", metadata.root)
        return metadata.__dict__.copy()

    def status(self) -> Dict[str, Any]:
        return {"started": self.started, "project": self.kernel.project.snapshot()}
