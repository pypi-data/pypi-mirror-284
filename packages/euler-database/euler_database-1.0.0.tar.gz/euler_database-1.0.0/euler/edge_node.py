"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
class Node:
    def __init__(self, id, label, properties=None, x=None, y=None):
        self.id = id
        self.label = label
        self.properties = properties
        self.x = x
        self.y = y

    def to_dict(self):
        return {
            'id': self.id,
            'label': self.label,
            'properties': self.properties
        }
    def __repr__(self):
        return f"Node(id={self.id}, label={self.label}, properties={self.properties})"

class Edge:
    def __init__(self, id, source, target, label, properties=None):
        self.id = id
        self.source = source
        self.target = target
        self.label = label
        self.properties = properties or {}

    def to_dict(self):
        return {
            'id': self.id,
            'source': self.source,
            'target': self.target,
            'label': self.label,
            'properties': self.properties
        }
    def __repr__(self):
        return f"Edge(id={self.id}, source={self.source}, target={self.target}, label={self.label}, properties={self.properties})"
