"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import json
import numpy as np
from euler.edge_node import Node, Edge
from collections import defaultdict

class GNNLayer(nn.Module):
    def __init__(self, in_features, out_features):
        super(GNNLayer, self).__init__()
        self.linear = nn.Linear(in_features, out_features)

    def forward(self, x, adj):
        h = torch.matmul(adj, x)
        h = self.linear(h)
        return h

class HashGNN(nn.Module):
    def __init__(self, in_features, hidden_features, out_features, num_layers):
        super(HashGNN, self).__init__()
        self.layers = nn.ModuleList()
        self.layers.append(GNNLayer(in_features, hidden_features))
        for _ in range(num_layers - 2):
            self.layers.append(GNNLayer(hidden_features, hidden_features))
        self.layers.append(GNNLayer(hidden_features, out_features))

    def forward(self, x, adj):
        for layer in self.layers:
            x = F.relu(layer(x, adj))
        return x

class HashGNNEmbedding:
    def __init__(self, graph, in_features=16, hidden_features=32, out_features=64, num_layers=3):
        self.graph = graph
        self.in_features = in_features
        self.hidden_features = hidden_features
        self.out_features = out_features
        self.num_layers = num_layers
        self.model = HashGNN(in_features, hidden_features, out_features, num_layers)
        self.embeddings = {}

    def generate_embeddings(self, epochs=100, learning_rate=0.01):
        node_ids = list(self.graph.nodes.keys())
        node_features = np.random.rand(len(node_ids), self.in_features).astype(np.float32)
        adj_matrix = self.build_adj_matrix(node_ids)

        node_features = torch.tensor(node_features)
        adj_matrix = torch.tensor(adj_matrix)

        optimizer = torch.optim.Adam(self.model.parameters(), lr=learning_rate)
        loss_fn = nn.MSELoss()

        for epoch in range(epochs):
            self.model.train()
            optimizer.zero_grad()
            output = self.model(node_features, adj_matrix)
            loss = loss_fn(output, node_features)  # Using node features as pseudo-targets
            loss.backward()
            optimizer.step()
            if (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item()}")

        self.model.eval()
        with torch.no_grad():
            embeddings = self.model(node_features, adj_matrix).numpy()

        self.embeddings = {node_id: embeddings[i].tolist() for i, node_id in enumerate(node_ids)}

    def build_adj_matrix(self, node_ids):
        size = len(node_ids)
        adj_matrix = np.zeros((size, size), dtype=np.float32)
        node_id_index = {node_id: idx for idx, node_id in enumerate(node_ids)}

        for edge in self.graph.edges.values():
            if edge.source in node_id_index and edge.target in node_id_index:
                src_idx = node_id_index[edge.source]
                tgt_idx = node_id_index[edge.target]
                adj_matrix[src_idx, tgt_idx] = 1.0
                adj_matrix[tgt_idx, src_idx] = 1.0  # Assuming undirected graph

        return adj_matrix

    def get_embedding(self, node_id):
        return self.embeddings.get(node_id)

    def save_embeddings(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.embeddings, file)

    def load_embeddings(self, file_path):
        with open(file_path, 'r') as file:
            self.embeddings = json.load(file)
