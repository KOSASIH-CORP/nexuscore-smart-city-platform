import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, num_heads, hidden_size, dropout):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.hidden_size = hidden_size
        self.dropout = dropout
        self.query_linear = nn.Linear(hidden_size, hidden_size)
        self.key_linear = nn.Linear(hidden_size, hidden_size)
        self.value_linear = nn.Linear(hidden_size, hidden_size)
        self.dropout_layer = nn.Dropout(dropout)

    def forward(self, query, key, value):
        batch_size = query.size(0)
        query = self.query_linear(query).view(batch_size, -1, self.num_heads, self.hidden_size // self.num_heads)
        key = self.key_linear(key).view(batch_size, -1, self.num_heads, self.hidden_size // self.num_heads)
        value = self.value_linear(value).view(batch_size, -1, self.num_heads, self.hidden_size // self.num_heads)
        attention_scores = torch.matmul(query, key.transpose(-1, -2)) / math.sqrt(self.hidden_size)
        attention_scores = F.softmax(attention_scores, dim=-1)
        attention_scores = self.dropout_layer(attention_scores)
        output = attention_scores * value
        output = output.view(batch_size, -1, self.hidden_size)
        return output
