# Nombre: process_service.py
# Fecha: 2026-06-29
# Utilidad: servicio permanente de procesos declarativos en SkillOAF Studio.
# API/Funcion asociada: ProcessService.run_catalog_process / run_json.
# Descripcion: encapsula catalogo, carga y ejecucion de procesos sobre ProcessEngine.
# Uso: service = ProcessService(kernel, session); service.run_catalog_process('flujo_base')
# Resultado esperado: proceso ejecutado y resultados devueltos.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from processes.engine import ProcessEngine
from processes.loader import ProcessLoader


class ProcessService:
    name = "process"

    def __init__(self, kernel: Any, session: Any | None = None) -> None:
        self.kernel = kernel
        self.session = session
        self.started = False

    def start(self) -> None:
        self.started = True

    def stop(self) -> None:
        self.started = False

    def bind_session(self, session: Any) -> None:
        self.session = session

    def run_catalog_process(self, process_name: str) -> List[Any]:
        if self.session is None:
            raise RuntimeError("ProcessService requiere una StudioSession para ejecutar procesos")
        item = self.kernel.process_catalog.get(process_name)
        process_path = self.kernel.project_root / Path(item.path)
        data = ProcessLoader.load_json(process_path)
        return ProcessEngine(self.session).run_dict(data)

    def run_json(self, process_path: str | Path) -> List[Any]:
        if self.session is None:
            raise RuntimeError("ProcessService requiere una StudioSession para ejecutar procesos")
        target = Path(process_path)
        if not target.is_absolute():
            target = self.kernel.project_root / target
        data = ProcessLoader.load_json(target)
        return ProcessEngine(self.session).run_dict(data)

    def status(self) -> Dict[str, Any]:
        return {
            "started": self.started,
            "session_bound": self.session is not None,
            "catalog": self.kernel.process_catalog.snapshot(),
        }
