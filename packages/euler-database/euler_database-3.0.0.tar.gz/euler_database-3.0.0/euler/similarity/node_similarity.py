"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

class NodeSimilarity:
    def __init__(self, graph, embedding_method="hashgnn", **embedding_params):
        self.graph = graph
        self.embeddings = None
        self.embedding_method = embedding_method
        self.embedding_params = embedding_params
        #self._generate_embeddings()

    def _generate_embeddings(self):
        self.graph.generate_embeddings(method=self.embedding_method, **self.embedding_params)
        self.embeddings = self.graph.embeddings.embeddings

    def get_embedding(self, node_id):
        return self.embeddings.get(node_id)

    def cosine_similarity(self, node_id1, node_id2):
        emb1 = self.get_embedding(node_id1)
        emb2 = self.get_embedding(node_id2)
        if emb1 is not None and emb2 is not None:
            return cosine_similarity([emb1], [emb2])[0][0]
        return None

    def jaccard_similarity(self, node_id1, node_id2):
        neighbors1 = set(self.graph.edge_source_index.get(node_id1, []))
        neighbors2 = set(self.graph.edge_source_index.get(node_id2, []))
        intersection = len(neighbors1 & neighbors2)
        union = len(neighbors1 | neighbors2)
        return intersection / union if union != 0 else 0

    def common_neighbors(self, node_id1, node_id2):
        neighbors1 = set(self.graph.edge_source_index.get(node_id1, []))
        neighbors2 = set(self.graph.edge_source_index.get(node_id2, []))
        return len(neighbors1 & neighbors2)

    def similarity_score(self, node_id1, node_id2, method="cosine"):
        if method == "cosine":
            return self.cosine_similarity(node_id1, node_id2)
        elif method == "jaccard":
            return self.jaccard_similarity(node_id1, node_id2)
        elif method == "common_neighbors":
            return self.common_neighbors(node_id1, node_id2)
        else:
            raise ValueError(f"Unknown similarity method: {method}")

    def most_similar_nodes(self, node_id, top_k=5, method="cosine"):
        scores = []
        for other_node_id in self.graph.nodes.keys():
            if other_node_id != node_id:
                score = self.similarity_score(node_id, other_node_id, method)
                if score is not None:
                    scores.append((other_node_id, score))
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]


if __name__ == "__main__":
    from euler.edge_node import Node, Edge
    from euler.knowlegde_graphy import KnowledgeGraph  # Assuming your KnowledgeGraph class is saved in knowledge_graph.py

    graph = KnowledgeGraph()
    graph.add_node(Node(id='1', label='Person', properties={'name': 'Alice', 'age': 30}))
    graph.add_node(Node(id='2', label='Person', properties={'name': 'Bob', 'age': 35}))
    graph.add_node(Node(id='3', label='Person', properties={'name': 'Carol', 'age': 40}))
    graph.add_edge(Edge(id='1-2', source='1', target='2', label='knows', properties={'since': '2020'}))
    graph.add_edge(Edge(id='2-3', source='2', target='3', label='knows', properties={'since': '2021'}))

    similarity = NodeSimilarity(graph, embedding_method="hashgnn", in_features=16, hidden_features=32, out_features=64, num_layers=3, epochs=100, learning_rate=0.01)

    print("Cosine similarity between node '1' and '2':", similarity.cosine_similarity('1', '2'))
    print("Jaccard similarity between node '1' and '3':", similarity.jaccard_similarity('1', '3'))
    print("Common neighbors between node '1' and '2':", similarity.common_neighbors('1', '2'))

    most_similar_to_node1 = similarity.most_similar_nodes('1', top_k=2, method="cosine")
    print("Most similar nodes to '1' using cosine similarity:", most_similar_to_node1)
