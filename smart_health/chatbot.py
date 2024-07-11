import nltk
from nltk.tokenize import word_tokenize
from sklearn.naive_bayes import MultinomialNB

class HealthChatbot:
    def __init__(self):
        self.classifier = MultinomialNB()

    def train(self, training_data):
        X = [word_tokenize(text) for text, _ in training_data]
        y = [label for _, label in training_data]
        self.classifier.fit(X, y)

    def predict(self, message):
        tokens = word_tokenize(message)
        return self.classifier.predict([tokens])[0]
