"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import json
from euler.edge_node import Node, Edge
from euler.graph_embedding.hash_gnn import HashGNNEmbedding 
from euler.graph_embedding.node2vec import GraphEmbeddings

class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.node_index = {}
        self.edge_source_index = {}
        self.edge_target_index = {}
        self.embeddings = None

    def add_node(self, node):
        self.nodes[node.id] = node
        self.node_index[node.id] = node

    def add_edge(self, edge):
        self.edges[edge.id] = edge
        if edge.source not in self.edge_source_index:
            self.edge_source_index[edge.source] = []
        if edge.target not in self.edge_target_index:
            self.edge_target_index[edge.target] = []
        self.edge_source_index[edge.source].append(edge)
        self.edge_target_index[edge.target].append(edge)

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def get_edges_by_node(self, node_id):
        edges = self.edge_source_index.get(node_id, []) + self.edge_target_index.get(node_id, [])
        return edges

    def get_nodes_by_label(self, label):
        return [node for node in self.nodes.values() if node.label == label]

    def get_edges_by_type(self, rel_type):
        return [edge for edge in self.edges.values() if edge.label == rel_type]

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump({
                'nodes': {id: node.to_dict() for id, node in self.nodes.items()},
                'edges': {id: edge.to_dict() for id, edge in self.edges.items()}
            }, file)

    def load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            for node_data in data['nodes'].values():
                node = Node(**node_data)
                self.add_node(node)
            for edge_data in data['edges'].values():
                edge = Edge(**edge_data)
                self.add_edge(edge)

    def generate_embeddings(self, method="simple", dimensions=64, **kwargs):
        if method == "simple":
            self.embeddings = GraphEmbeddings(self)
            self.embeddings.generate_simple_embeddings(dimensions)
        elif method == "node2vec":
            self.embeddings = GraphEmbeddings(self)
            self.embeddings.generate_node2vec_embeddings(dimensions, **kwargs)
        elif method == "openai":
            self.embeddings = GraphEmbeddings(self)
            self.embeddings.generate_openai_embeddings(**kwargs)
        elif method == "huggingface":
            self.embeddings = GraphEmbeddings(self)
            self.embeddings.generate_huggingface_embeddings(**kwargs)
        elif method == "hashgnn":
            self.embeddings = HashGNNEmbedding(self, **kwargs)
            self.embeddings.generate_embeddings(**kwargs)
        else:
            raise ValueError(f"Unknown embedding method: {method}")

    def get_embedding(self, node_id):
        if not self.embeddings:
            raise ValueError("Embeddings not generated yet. Call generate_embeddings() first.")
        return self.embeddings.get_embedding(node_id)

    def save_embeddings(self, file_path):
        if not self.embeddings:
            raise ValueError("Embeddings not generated yet. Call generate_embeddings() first.")
        self.embeddings.save_embeddings(file_path)

    def load_embeddings(self, file_path):
        self.embeddings = GraphEmbeddings(self)
        self.embeddings.load_embeddings(file_path)



if __name__ == "__main__":
    graph = KnowledgeGraph()
    graph.add_node(Node(id='1', label='Person', properties={'name': 'Alice', 'age': 30}))
    graph.add_node(Node(id='2', label='Person', properties={'name': 'Bob', 'age': 35}))
    graph.add_edge(Edge(id='1-2', source='1', target='2', label='knows', properties={'since': '2020'}))

    graph.generate_embeddings(method="simple")
    print("Simple embedding for node '1':", graph.get_embedding('1'))

    graph.generate_embeddings(method="node2vec", dimensions=64, walk_length=30, num_walks=200, workers=4)
    print("Node2Vec embedding for node '1':", graph.get_embedding('1'))

    graph.generate_embeddings(method="openai", model_name="text-embedding-ada-002")
    print("OpenAI embedding for node '1':", graph.get_embedding('1'))

    graph.generate_embeddings(method="huggingface", model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("Hugging Face embedding for node '1':", graph.get_embedding('1'))

    graph.save_to_file("graph.json")
    graph.save_embeddings("embeddings.json")

    new_graph = KnowledgeGraph()
    new_graph.load_from_file("graph.json")
    new_graph.load_embeddings("embeddings.json")
    print("Loaded embedding for node '1':", new_graph.get_embedding('1'))
