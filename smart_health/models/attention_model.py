import torch
import torch.nn as nn

class AttentionModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(AttentionModel, self).__init__()
        self.query_linear = nn.Linear(input_dim, hidden_dim)
        self.key_linear = nn.Linear(input_dim, hidden_dim)
        self.value_linear = nn.Linear(input_dim, hidden_dim)
        self.dropout = nn.Dropout(0.1)

    def forward(self, input_seq):
        query = self.query_linear(input_seq)
        key = self.key_linear(input_seq)
        value = self.value_linear(input_seq)
        attention_scores = torch.matmul(query, key.T) / math.sqrt(hidden_dim)
        attention_scores = self.dropout(attention_scores)
        attention_weights = F.softmax(attention_scores, dim=-1)
        output = attention_weights * value
        return output
