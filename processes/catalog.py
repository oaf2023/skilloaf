# Nombre: catalog.py
# Fecha: 2026-06-29
# Utilidad: catalogo oficial de procesos declarativos para SkillOAF Studio.
# API/Funcion asociada: ProcessCatalog.register / get / default.
# Descripcion: administra procesos disponibles, versiones y rutas declarativas.
# Uso: catalog = ProcessCatalog.default(); catalog.get('flujo_base')
# Resultado esperado: descriptor de proceso disponible para carga y ejecucion.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass
class ProcessCatalogItem:
    name: str
    version: str
    description: str
    path: str


class ProcessCatalog:
    def __init__(self) -> None:
        self._items: Dict[str, ProcessCatalogItem] = {}

    def register(self, item: ProcessCatalogItem) -> None:
        self._items[item.name] = item

    def get(self, name: str) -> ProcessCatalogItem:
        if name not in self._items:
            raise KeyError(f"Proceso no registrado: {name}")
        return self._items[name]

    def names(self) -> List[str]:
        return sorted(self._items.keys())

    def snapshot(self) -> List[dict]:
        return [item.__dict__.copy() for item in self._items.values()]

    @classmethod
    def default(cls) -> "ProcessCatalog":
        catalog = cls()
        catalog.register(
            ProcessCatalogItem(
                name="flujo_base",
                version="0.2.0",
                description="Proceso base de SkillOAF Studio con agentes principales.",
                path=str(Path("processes") / "templates" / "flujo_base.json"),
            )
        )
        return catalog
