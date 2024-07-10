import torch
import torch.nn as nn
import torch.nn.functional as F

class BERTLanguageModel(nn.Module):
    def __init__(self, vocab_size, hidden_size, num_layers, num_heads):
        super(BERTLanguageModel, self).__init__()
        self.vocab_size = vocab_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.num_heads = num_heads
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        self.encoder = nn.TransformerEncoderLayer(d_model=hidden_size, nhead=num_heads, dim_feedforward=hidden_size, dropout=0.1)
        self.decoder = nn.TransformerDecoderLayer(d_model=hidden_size, nhead=num_heads, dim_feedforward=hidden_size, dropout=0.1)

    def forward(self, input_ids, attention_mask):
        embeddings = self.embedding(input_ids)
        encoder_output = self.encoder(embeddings, attention_mask)
        decoder_output = self.decoder(encoder_output, attention_mask)
        return decoder_output

    def generate_text(self, input_ids, attention_mask, max_length):
        output = self.forward(input_ids, attention_mask)
        generated_text = []
        for i in range(max_length):
            next_token = torch.argmax(output[:, i, :])
            generated_text.append(next_token.item())
            output = self.forward(torch.tensor([generated_text]), attention_mask)
        return generated_text
