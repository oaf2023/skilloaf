# Nombre: artifact_service.py
# Fecha: 2026-06-29
# Utilidad: servicio permanente de gobierno de artefactos en SkillOAF Studio.
# API/Funcion asociada: ArtifactService.write / list.
# Descripcion: encapsula ArtifactEngine para registrar y consultar artefactos generados.
# Uso: service = ArtifactService(kernel); service.write('output/docs/demo.md', '# Demo', 'docs')
# Resultado esperado: artefacto creado y registrado.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Any, Dict


class ArtifactService:
    name = "artifact"

    def __init__(self, kernel: Any) -> None:
        self.kernel = kernel
        self.started = False

    def start(self) -> None:
        self.started = True

    def stop(self) -> None:
        self.started = False

    def write(self, relative_path: str, content: str, kind: str, producer: str = "artifact_service") -> Any:
        artifact = self.kernel.artifacts.write(relative_path, content, kind, producer)
        self.kernel.events.publish("artifact_created", {"path": artifact.path, "kind": artifact.kind})
        return artifact

    def list(self) -> Dict[str, list[str]]:
        return self.kernel.artifacts.as_dict()

    def status(self) -> Dict[str, Any]:
        return {"started": self.started, "artifacts": self.kernel.artifacts.as_dict()}
