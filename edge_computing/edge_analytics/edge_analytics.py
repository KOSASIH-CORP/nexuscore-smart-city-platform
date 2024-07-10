import pandas as pd
from sklearn.model_selection import train_test_split

class EdgeAnalytics:
    def __init__(self, dataset):
        self.dataset = dataset

    def train_model(self):
        X = self.dataset.drop('target', axis=1)
        y = self.dataset['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model

    def predict(self, model, data):
        return model.predict(data)
