# Nombre: service_manager.py
# Fecha: 2026-06-29
# Utilidad: registro y ciclo de vida de servicios fundacionales de SkillOAF Studio.
# API/Funcion asociada: ServiceManager.register / get / start_all.
# Descripcion: centraliza servicios permanentes para desacoplar capacidades del Kernel.
# Uso: manager = ServiceManager(kernel); manager.register('project', ProjectService(kernel)); manager.start_all()
# Resultado esperado: servicios registrados, iniciados y disponibles por nombre.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Protocol


class Service(Protocol):
    name: str

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...

    def status(self) -> Dict[str, Any]:
        ...


@dataclass
class ServiceDescriptor:
    name: str
    status: str
    service: Service


class ServiceManager:
    def __init__(self, kernel: Any) -> None:
        self.kernel = kernel
        self._services: Dict[str, ServiceDescriptor] = {}

    def register(self, name: str, service: Service) -> None:
        self._services[name] = ServiceDescriptor(name=name, status="registered", service=service)

    def get(self, name: str) -> Service:
        if name not in self._services:
            raise KeyError(f"Servicio no registrado: {name}")
        return self._services[name].service

    def start_all(self) -> None:
        for descriptor in self._services.values():
            descriptor.service.start()
            descriptor.status = "started"
            if hasattr(self.kernel, "events"):
                self.kernel.events.publish("service_started", {"service": descriptor.name})

    def stop_all(self) -> None:
        for descriptor in self._services.values():
            descriptor.service.stop()
            descriptor.status = "stopped"
            if hasattr(self.kernel, "events"):
                self.kernel.events.publish("service_stopped", {"service": descriptor.name})

    def names(self) -> List[str]:
        return sorted(self._services.keys())

    def snapshot(self) -> List[Dict[str, Any]]:
        return [
            {"name": item.name, "status": item.status, "detail": item.service.status()}
            for item in self._services.values()
        ]
