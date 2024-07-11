import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class HealthModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
