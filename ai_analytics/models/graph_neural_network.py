import torch
import torch.nn as nn
import torch.optim as optim

class GraphNeuralNetwork(nn.Module):
    def __init__(self):
        super(GraphNeuralNetwork, self).__init__()
        self.conv1 = nn.GraphConv(10, 20)
        self.conv2 = nn.GraphConv(20, 30)
        self.fc = nn.Linear(30, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = self.fc(x)
        return x

    def train(self, data):
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(self.parameters(), lr=0.001)

        for epoch in range(10):
            for batch in data:
                x, y = batch
                x = x.to(device)
                y = y.to(device)
                optimizer.zero_grad()
                output = self.forward(x)
                loss = criterion(output, y)
                loss.backward()
                optimizer.step()

    def evaluate(self, data):
        total_correct = 0
        with torch.no_grad():
            for batch in data:
                x, y = batch
                x = x.to(device)
                y = y.to(device)
                output = self.forward(x)
                _, predicted = torch.max(output, 1)
                total_correct += (predicted == y).sum().item()

        accuracy = total_correct / len(data)
        return accuracy
