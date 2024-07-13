"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import json
import matplotlib.pyplot as plt
import networkx as nx
from euler.edge_node import Node, Edge
from euler.knowlegde_graphy import KnowledgeGraph
from euler.query_engine import QueryEngine

class KnowledgeGraphAPI:
    def __init__(self):
        self.graph = KnowledgeGraph()
        self.query_engine = QueryEngine(self.graph)

    def create_node(self, id, label, properties=None):
        node = Node(id, label, properties)
        self.graph.add_node(node)
        return node

    def create_edge(self, id, source, target, label, properties=None):
        edge = Edge(id, source, target, label, properties)
        self.graph.add_edge(edge)
        return edge

    def get_node(self, id):
        return self.query_engine.get_node_by_id(id)

    def get_node_edges(self, id):
        return self.query_engine.get_edges_by_node(id)

    def save_graph(self, file_path):
        self.graph.save_to_file(file_path)

    def load_graph(self, file_path):
        self.graph.load_from_file(file_path)

    # def get_graph_json(self):
    #     return json.dumps({
    #         "nodes": {id: node.to_dict() for id, node in self.graph.nodes.items()},
    #         "edges": {id: edge.to_dict() for id, edge in self.graph.edges.items()}
    #     }, indent=4)
    
    def get_graph_json(self):
        if self.graph:
            serializable_graph = self.serialize_graph()
            return json.dumps(serializable_graph, indent=4)
        else:
            return "Graph data not available."

    def serialize_graph(self):
        serialized_graph = {
            'nodes': [],
            'edges': []
        }
        for node_id, node in self.graph.nodes.items():
            serialized_node = {
                'id': node.id,
                'label': node.label,
                'properties': node.properties
            }
            serialized_graph['nodes'].append(serialized_node)
        for edge_id, edge in self.graph.edges.items():
            serialized_edge = {
                'id': edge.id,
                'source': edge.source,
                'target': edge.target,
                'label': edge.label,
                'properties': edge.properties
            }
            serialized_graph['edges'].append(serialized_edge)
        return serialized_graph

    def visualize_graph(self, file_path='graph.png'):
        print("Visualization started")
        G = nx.Graph()

        for node_id, node in self.graph.nodes.items():
            G.add_node(node_id)
        for edge_id, edge in self.graph.edges.items():
            G.add_edge(edge.source, edge.target)

        pos = nx.fruchterman_reingold_layout(G)

        plt.figure(figsize=(12, 8))  # Increase the figure size

        nx.draw_networkx_nodes(G, pos, node_size=500, node_color='blue')
        nx.draw_networkx_edges(G, pos, width=2, edge_color='#888')

        # node_labels = nx.get_node_attributes(G, 'label')
        # edge_labels = nx.get_edge_attributes(G, 'label')
        # print("node- labels", node_labels)
        # print("edge - labels", edge_labels)

        node_labels = {node: f"{self.graph.nodes[node].label}\n{self.graph.nodes[node].properties}" for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='black')
        plt.axis('off')
        plt.savefig(file_path)
        plt.close()

        print("Visualization completed")

