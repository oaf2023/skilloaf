# Nombre: knowledge_service.py
# Fecha: 2026-06-29
# Utilidad: servicio inicial de conocimiento para SkillOAF Studio.
# API/Funcion asociada: KnowledgeService.add_node / add_relation / snapshot.
# Descripcion: inicia una base de conocimiento simple que servira como base del futuro Project Digital Twin.
# Uso: service.add_node('entity','Cliente'); service.add_relation('Cliente','usa','API Clientes')
# Resultado esperado: nodos y relaciones disponibles en memoria.
# Conexion API: no conecta a APIs externas.

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List


@dataclass
class KnowledgeNode:
    kind: str
    name: str
    data: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


@dataclass
class KnowledgeRelation:
    source: str
    relation: str
    target: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


class KnowledgeService:
    name = "knowledge"

    def __init__(self, kernel: Any) -> None:
        self.kernel = kernel
        self.started = False
        self.nodes: List[KnowledgeNode] = []
        self.relations: List[KnowledgeRelation] = []

    def start(self) -> None:
        self.started = True

    def stop(self) -> None:
        self.started = False

    def add_node(self, kind: str, name: str, data: Dict[str, Any] | None = None) -> KnowledgeNode:
        node = KnowledgeNode(kind=kind, name=name, data=data or {})
        self.nodes.append(node)
        self.kernel.events.publish("knowledge_node_added", {"kind": kind, "name": name})
        return node

    def add_relation(self, source: str, relation: str, target: str) -> KnowledgeRelation:
        item = KnowledgeRelation(source=source, relation=relation, target=target)
        self.relations.append(item)
        self.kernel.events.publish("knowledge_relation_added", {"source": source, "relation": relation, "target": target})
        return item

    def snapshot(self) -> Dict[str, Any]:
        return {
            "nodes": [node.__dict__ for node in self.nodes],
            "relations": [relation.__dict__ for relation in self.relations],
        }

    def status(self) -> Dict[str, Any]:
        data = self.snapshot()
        return {"started": self.started, "nodes": len(data["nodes"]), "relations": len(data["relations"])}
