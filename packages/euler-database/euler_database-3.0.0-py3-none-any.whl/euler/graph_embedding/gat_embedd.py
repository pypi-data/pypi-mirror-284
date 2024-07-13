import torch
import torch.nn.functional as F
from torch_geometric.nn import GATConv
from torch_geometric.data import Data
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
edge_index = torch.tensor(list(G.edges), dtype=torch.long).t().contiguous()
x = torch.eye(G.number_of_nodes(), dtype=torch.float)

data = Data(x=x, edge_index=edge_index)
class GAT(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super(GAT, self).__init__()
        self.conv1 = GATConv(in_channels, 8, heads=8, dropout=0.6)
        self.conv2 = GATConv(8 * 8, out_channels, heads=1, concat=False, dropout=0.6)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.dropout(x, p=0.6, training=self.training)
        x = self.conv1(x, edge_index)
        x = F.elu(x)
        x = F.dropout(x, p=0.6, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# Instantiate and train the model
model = GAT(in_channels=G.number_of_nodes(), out_channels=4)  # Assume 4 classes for the output
optimizer = torch.optim.Adam(model.parameters(), lr=0.005, weight_decay=5e-4)

model.train()
for epoch in range(200):
    optimizer.zero_grad()
    out = model(data)
    loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()

# Get the embedding for a node
model.eval()
node_id = 0
embedding = model(data)[node_id].detach().numpy()
print(f"Embedding for node {node_id}: {embedding}")
