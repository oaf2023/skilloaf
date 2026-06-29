# Nombre: artifact_engine.py
# Fecha: 2026-06-29
# Utilidad: motor de artefactos para SkillOAF Studio.
# API/Funcion asociada: ArtifactEngine.write / ArtifactEngine.register.
# Descripcion: registra, crea y lista artefactos generados por agentes dentro del proyecto.
# Uso: engine.write('docs/demo.md', '# Demo', 'documentacion')
# Resultado esperado: archivo creado y artefacto registrado en memoria interna.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List


@dataclass
class Artifact:
    path: str
    kind: str
    producer: str = "kernel"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


class ArtifactEngine:
    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root
        self.artifacts: List[Artifact] = []

    def register(self, relative_path: str, kind: str, producer: str = "kernel") -> Artifact:
        artifact = Artifact(path=relative_path, kind=kind, producer=producer)
        self.artifacts.append(artifact)
        return artifact

    def write(self, relative_path: str, content: str, kind: str, producer: str = "kernel") -> Artifact:
        target = self.project_root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return self.register(relative_path, kind, producer)

    def list_by_kind(self, kind: str) -> List[Artifact]:
        return [artifact for artifact in self.artifacts if artifact.kind == kind]

    def as_dict(self) -> Dict[str, List[str]]:
        result: Dict[str, List[str]] = {}
        for artifact in self.artifacts:
            result.setdefault(artifact.kind, []).append(artifact.path)
        return result
