from euler.knowlegde_graphy import KnowledgeGraph
from euler.edge_node import Node, Edge
from euler.similarity.node_similarity import NodeSimilarity

# Create a KnowledgeGraph instance
graph = KnowledgeGraph()

# Add nodes and edges
graph.add_node(Node(id='1', label='Person', properties={'name': 'Alice', 'age': 30}))
graph.add_node(Node(id='2', label='Person', properties={'name': 'Bob', 'age': 35}))
graph.add_node(Node(id='3', label='Person', properties={'name': 'Carol', 'age': 40}))
graph.add_edge(Edge(id='1-2', source='1', target='2', label='knows', properties={'since': '2020'}))
graph.add_edge(Edge(id='2-3', source='2', target='3', label='knows', properties={'since': '2021'}))

# Initialize NodeSimilarity with the graph
similarity = NodeSimilarity(graph, embedding_method="hashgnn", in_features=16, hidden_features=32, out_features=64, num_layers=3, epochs=100, learning_rate=0.01)

# Calculate similarities
print("Cosine similarity between node '1' and '2':", similarity.cosine_similarity('1', '2'))
print("Jaccard similarity between node '1' and '3':", similarity.jaccard_similarity('1', '3'))
print("Common neighbors between node '1' and '2':", similarity.common_neighbors('1', '2'))

# Find most similar nodes
most_similar_to_node1 = similarity.most_similar_nodes('1', top_k=2, method="cosine")
print("Most similar nodes to '1' using cosine similarity:", most_similar_to_node1)
