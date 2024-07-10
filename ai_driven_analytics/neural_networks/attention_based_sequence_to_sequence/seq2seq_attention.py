import torch
import torch.nn as nn
import torch.nn.functional as F

class Seq2SeqAttention(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers, dropout):
        super(Seq2SeqAttention, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.num_layers = num_layers
        self.dropout = dropout
        self.encoder = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True, dropout=dropout)
        self.decoder = nn.LSTM(hidden_dim, output_dim, num_layers, batch_first=True, dropout=dropout)
        self.attention = nn.MultiHeadAttention(hidden_dim, hidden_dim)

    def forward(self, input_seq, output_seq):
        encoder_output, _ = self.encoder(input_seq)
        decoder_output, _ = self.decoder(output_seq, encoder_output)
        attention_output = self.attention(decoder_output, encoder_output)
        return attention_output

    def generate_sequence(self, input_seq, max_length):
        encoder_output, _ = self.encoder(input_seq)
        decoder_output = torch.zeros((1, max_length, self.output_dim))
        for i in range(max_length):
            decoder_output[:, i, :] = self.decoder(decoder_output[:, i-1, :], encoder_output)
            attention_output = self.attention(decoder_output[:, i, :], encoder_output)
            decoder_output[:, i, :] = attention_output
        return decoder_output
