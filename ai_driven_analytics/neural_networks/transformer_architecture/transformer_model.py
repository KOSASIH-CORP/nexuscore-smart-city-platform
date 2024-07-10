import torch
import torch.nn as nn
import torch.nn.functional as F

class TransformerModel(nn.Module):
    def __init__(self, num_layers, hidden_size, output_size, dropout):
        super(TransformerModel, self).__init__()
        self.encoder = TransformerEncoderLayer(d_model=hidden_size, nhead=8, dim_feedforward=hidden_size, dropout=dropout)
        self.decoder = TransformerDecoderLayer(d_model=hidden_size, nhead=8, dim_feedforward=hidden_size, dropout=dropout)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, src, tgt):
        src = self.encoder(src)
        tgt = self.decoder(tgt, src)
        output = self.fc(tgt)
        return output
