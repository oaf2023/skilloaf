# Nombre: event_bus.py
# Fecha: 2026-06-29
# Utilidad: bus de eventos interno para SkillOAF Studio.
# API/Funcion asociada: EventBus.publish / EventBus.subscribe.
# Descripcion: permite publicar eventos del proyecto y que distintos componentes reaccionen desacoplados.
# Uso: bus.subscribe('proyecto_creado', handler); bus.publish('proyecto_creado', {'nombre':'Demo'})
# Resultado esperado: los handlers suscriptos reciben el evento.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, DefaultDict, Dict, List


@dataclass
class Event:
    name: str
    payload: Dict[str, Any]
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


class EventBus:
    def __init__(self) -> None:
        self._subscribers: DefaultDict[str, List[Callable[[Event], None]]] = defaultdict(list)
        self.history: List[Event] = []

    def subscribe(self, event_name: str, handler: Callable[[Event], None]) -> None:
        self._subscribers[event_name].append(handler)

    def publish(self, event_name: str, payload: Dict[str, Any] | None = None) -> Event:
        event = Event(name=event_name, payload=payload or {})
        self.history.append(event)
        handlers = list(self._subscribers.get(event_name, [])) + list(self._subscribers.get("*", []))

        if sys.version_info > (3, 13) and len(handlers) > 1:
            with ThreadPoolExecutor() as executor:
                list(executor.map(lambda h: h(event), handlers))
        else:
            for handler in handlers:
                handler(event)

        return event
