"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
from euler.edge_node import Edge

class RelationshipManager:
    def __init__(self, graph):
        self.graph = graph

    def create_relationship(self, source, target, label, properties=None):
        properties = properties if properties else {}
        edge_id = f"{source}-{label}-{target}"
        if (source in self.graph.node_index and target in self.graph.node_index) or (edge_id):
            edge = Edge(edge_id, source, target, label, properties)
            self.graph.add_edge(edge)
            print(f"Edge ({source})-[:{label}]->({target}) created successfully.")
            return f"Edge ({source})-[:{label}]->({target}) created successfully."
        else:
            return f"Error: Either source node {source} or target node {target} does not exist."

    def get_relationships(self, node_id):
        if node_id in self.graph.node_index:
            return self.graph.get_edges_by_node(node_id)
        else:
            return f"Error: Node with ID {node_id} not found in the graph."
