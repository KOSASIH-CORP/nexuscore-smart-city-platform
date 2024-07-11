import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

class TransformerModel(nn.Module):
    def __init__(self):
        super(TransformerModel, self).__init__()
        self.encoder = nn.TransformerEncoderLayer(d_model=512, nhead=8, dim_feedforward=2048, dropout=0.1)
        self.decoder = nn.TransformerDecoderLayer(d_model=512, nhead=8, dim_feedforward=2048, dropout=0.1)
        self.fc = nn.Linear(512, 10)

    def forward(self, src, tgt):
        src = self.encoder(src)
        tgt = self.decoder(tgt, src)
        output = self.fc(tgt)
        return output

    def train(self, data):
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(self.parameters(), lr=0.001)

        for epoch in range(10):
            for batch in data:
                src, tgt = batch
                src = src.to(device)
                tgt = tgt.to(device)
                optimizer.zero_grad()
                output = self.forward(src, tgt)
                loss = criterion(output, tgt)
                loss.backward()
                optimizer.step()

    def evaluate(self, data):
        total_correct = 0
        with torch.no_grad():
            for batch in data:
                src, tgt = batch
                src = src.to(device)
                tgt = tgt.to(device)
                output = self.forward(src, tgt)
                _, predicted = torch.max(output, 1)
                total_correct += (predicted == tgt).sum().item()

        accuracy = total_correct / len(data)
        return accuracy
