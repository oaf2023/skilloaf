# Nombre: metrics.py
# Fecha: 2026-06-29
# Utilidad: motor de metricas internas para SkillOAF Studio.
# API/Funcion asociada: MetricsEngine.increment / set / snapshot.
# Descripcion: guarda contadores y valores operativos del Kernel, Runtime y Agentes.
# Uso: metrics.increment('agents.completed')
# Resultado esperado: metrica actualizada en memoria.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from typing import Dict, Union

MetricValue = Union[int, float, str]


class MetricsEngine:
    def __init__(self) -> None:
        self._metrics: Dict[str, MetricValue] = {}

    def increment(self, key: str, amount: int = 1) -> None:
        current = self._metrics.get(key, 0)
        if isinstance(current, (int, float)):
            self._metrics[key] = current + amount
        else:
            self._metrics[key] = amount

    def set(self, key: str, value: MetricValue) -> None:
        self._metrics[key] = value

    def get(self, key: str, default: MetricValue = 0) -> MetricValue:
        return self._metrics.get(key, default)

    def snapshot(self) -> Dict[str, MetricValue]:
        return dict(self._metrics)
