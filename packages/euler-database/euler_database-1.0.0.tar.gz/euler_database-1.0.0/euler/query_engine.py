"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
from euler.knowlegde_graphy import KnowledgeGraph

class QueryEngine:
    def __init__(self, graph):
        self.graph = graph

    def get_node_by_id(self, node_id):
        return self.graph.get_node(node_id)

    def get_edges_by_node(self, node_id):
        return self.graph.get_edges_by_node(node_id)
