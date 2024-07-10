import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class IntrusionDetection:
    def __init__(self, training_data):
        self.training_data = training_data
        self.classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    
    def train_classifier(self):
        # Train classifier using training data
        X = self.training_data.drop('label', axis=1)
        y = self.training_data['label']
        self.classifier.fit(X, y)
    
    def detect_intrusion(self, new_data):
        # Detect intrusion using trained classifier
        prediction = self.classifier.predict(new_data)
        return prediction
    
    def evaluate_performance(self, test_data):
        # Evaluate performance of intrusion detection system
        X = test_data.drop('label', axis=1)
        y = test_data['label']
        prediction = self.classifier.predict(X)
        accuracy = accuracy_score(y, prediction)
        return accuracy
