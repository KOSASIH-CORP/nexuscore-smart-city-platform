import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class AdvancedThreatDetection:
    def __init__(self, training_data):
        self.training_data = training_data
        self.model = self.create_model()
    
    def create_model(self):
        # Create advanced threat detection model using random forest classifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        return model
    
    def train_model(self):
        # Train advanced threat detection model using training data
        X = self.training_data.drop('label', axis=1)
        y = self.training_data['label']
        self.model.fit(X, y)
    
    def detect_threats(self, new_data):
        # Detect threats using trained model
        prediction = self.model.predict(new_data)
        return prediction
    
    def evaluate_performance(self, test_data):
        # Evaluate performance of advanced threat detection model
        X = test_data.drop('label', axis=1)
        y = test_data['label']
        prediction = self.model.predict(X)
        accuracy = accuracy_score(y, prediction)
        return accuracy
