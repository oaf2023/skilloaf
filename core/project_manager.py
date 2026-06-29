# Nombre: project_manager.py
# Fecha: 2026-06-29
# Utilidad: gestor de proyectos para SkillOAF Studio.
# API/Funcion asociada: ProjectManager.open_project / ensure_governance_files.
# Descripcion: administra raiz de proyecto, metadatos y archivos minimos de gobierno documental.
# Uso: pm = ProjectManager('.'); pm.open_project()
# Resultado esperado: proyecto abierto y archivos de gobierno verificados.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict


@dataclass
class ProjectMetadata:
    name: str
    root: str
    opened_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


class ProjectManager:
    GOVERNANCE_FILES = {
        "datos.md": "# datos.md\n\nGuia ejecutiva del proyecto.\n",
        "memoria.md": "# memoria.md\n\nDecisiones tomadas del proyecto.\n",
        "reglas.md": "# reglas.md\n\nReglas permanentes del proyecto.\n",
        "backlog.md": "# backlog.md\n\nPendientes y evolucion.\n",
        "cambios.md": "# cambios.md\n\nHistorial de cambios.\n",
    }

    def __init__(self, project_root: str | Path) -> None:
        self.project_root = Path(project_root).resolve()
        self.metadata: ProjectMetadata | None = None

    def open_project(self) -> ProjectMetadata:
        self.project_root.mkdir(parents=True, exist_ok=True)
        self.ensure_structure()
        self.ensure_governance_files()
        self.metadata = ProjectMetadata(name=self.project_root.name, root=str(self.project_root))
        return self.metadata

    def ensure_structure(self) -> None:
        folders = [
            "requirements/assets",
            "output/frontend",
            "output/backend",
            "output/database",
            "output/docs",
            "output/diagrams",
            "output/tests",
            "output/deploy",
            "logs",
        ]
        for folder in folders:
            (self.project_root / folder).mkdir(parents=True, exist_ok=True)

    def ensure_governance_files(self) -> None:
        for relative_path, content in self.GOVERNANCE_FILES.items():
            target = self.project_root / relative_path
            if not target.exists():
                target.write_text(content, encoding="utf-8")

    def snapshot(self) -> Dict[str, str]:
        if self.metadata is None:
            return {"status": "not_open", "root": str(self.project_root)}
        return self.metadata.__dict__.copy()
