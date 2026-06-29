# Nombre: logging_engine.py
# Fecha: 2026-06-29
# Utilidad: motor de logging interno para SkillOAF Studio.
# API/Funcion asociada: LoggingEngine.info / warning / error.
# Descripcion: registra eventos operativos simples en memoria y opcionalmente en archivo.
# Uso: logger.info('Kernel iniciado')
# Resultado esperado: entrada de log registrada.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List


@dataclass
class LogEntry:
    level: str
    message: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


class LoggingEngine:
    def __init__(self, project_root: Path | None = None) -> None:
        self.project_root = project_root
        self.entries: List[LogEntry] = []

    def log(self, level: str, message: str) -> None:
        entry = LogEntry(level=level.upper(), message=message)
        self.entries.append(entry)
        if self.project_root is not None:
            path = self.project_root / "logs" / "skilloaf.log"
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("a", encoding="utf-8") as file:
                file.write(f"{entry.created_at} [{entry.level}] {entry.message}\n")

    def info(self, message: str) -> None:
        self.log("INFO", message)

    def warning(self, message: str) -> None:
        self.log("WARNING", message)

    def error(self, message: str) -> None:
        self.log("ERROR", message)
