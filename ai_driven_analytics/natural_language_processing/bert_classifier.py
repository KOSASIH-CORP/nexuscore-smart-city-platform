import torch
import transformers

class BERTClassifier:
    def __init__(self, model_name, num_labels):
        self.model_name = model_name
        self.num_labels = num_labels
        self.model = transformers.BertForSequenceClassification.from_pretrained(self.model_name, num_labels=self.num_labels)

    def inference(self, input_ids, attention_mask):
        output = self.model(input_ids, attention_mask=attention_mask)
        logits = output.logits
        probabilities = torch.nn.functional.softmax(logits, dim=1)
        return probabilities
