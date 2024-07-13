"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import json
import numpy as np
from euler.edge_node import Node, Edge
from node2vec import Node2Vec  
import openai
from transformers import AutoTokenizer, AutoModel

class GraphEmbeddings:
    def __init__(self, graph):
        self.graph = graph
        self.embeddings = {}

    def generate_simple_embeddings(self, dimensions=64):
        self.embeddings = {node_id: np.random.rand(dimensions).tolist() for node_id in self.graph.nodes}

    def generate_node2vec_embeddings(self, dimensions=64, walk_length=30, num_walks=200, workers=4):
        # Create the edge list for node2vec
        edge_list = [(edge.source, edge.target) for edge in self.graph.edges.values()]
        node2vec = Node2Vec(edge_list, dimensions=dimensions, walk_length=walk_length, num_walks=num_walks, workers=workers)
        model = node2vec.fit(window=10, min_count=1, batch_words=4)
        self.embeddings = {str(node_id): model.wv[str(node_id)].tolist() for node_id in self.graph.nodes}

    def generate_openai_embeddings(self, model_name="text-embedding-ada-002"):
        openai.api_key = 'your-openai-api-key'
        embeddings = {}
        for node_id, node in self.graph.nodes.items():
            text = json.dumps(node.to_dict())
            response = openai.Embedding.create(input=text, model=model_name)
            embeddings[node_id] = response['data'][0]['embedding']
        self.embeddings = embeddings

    def generate_huggingface_embeddings(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name)
        embeddings = {}
        for node_id, node in self.graph.nodes.items():
            text = json.dumps(node.to_dict())
            inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
            outputs = model(**inputs)
            embeddings[node_id] = outputs.last_hidden_state.mean(dim=1).detach().numpy().tolist()[0]
        self.embeddings = embeddings

    def get_embedding(self, node_id):
        return self.embeddings.get(str(node_id))

    def save_embeddings(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.embeddings, file)

    def load_embeddings(self, file_path):
        with open(file_path, 'r') as file:
            self.embeddings = json.load(file)
