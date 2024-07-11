import torch
import torch.nn as nn
import torch_geometric.nn as pyg_nn
import torch_geometric.data as pyg_data

class GraphNeuralNetwork(nn.Module):
    def __init__(self, num_layers, hidden_dim, output_dim):
        super(GraphNeuralNetwork, self).__init__()
        self.layers = nn.ModuleList([GraphConvLayer(hidden_dim, hidden_dim) for _ in range(num_layers)])
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, data):
        x, edge_index, batch = data.x, data.edge_index, data.batch
        for layer in self.layers:
            x = layer(x, edge_index)
        x = self.fc(x)
        return x

class GraphConvLayer(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(GraphConvLayer, self).__init__()
        self.conv = pyg_nn.GraphConv(input_dim, hidden_dim)

    def forward(self, x, edge_index):
        x = self.conv(x, edge_index)
        return x
