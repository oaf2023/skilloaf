# Nombre: configuration.py
# Fecha: 2026-06-29
# Utilidad: gestor de configuracion del core SkillOAF Studio.
# API/Funcion asociada: ConfigurationManager.load_defaults / get / set.
# Descripcion: administra configuracion interna del Kernel sin depender de archivos externos.
# Uso: config = ConfigurationManager(); config.set('runtime.mode','local')
# Resultado esperado: configuracion disponible para servicios y agentes.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Any, Dict


class ConfigurationManager:
    def __init__(self) -> None:
        self._values: Dict[str, Any] = {}
        self.load_defaults()

    def load_defaults(self) -> None:
        self._values.update(
            {
                "runtime.mode": "local",
                "runtime.version": "0.2.0",
                "agents.autoload": True,
                "processes.default": "processes/templates/flujo_base.json",
                "artifacts.output_dir": "output",
            }
        )

    def get(self, key: str, default: Any = None) -> Any:
        return self._values.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._values[key] = value

    def all(self) -> Dict[str, Any]:
        return dict(self._values)
