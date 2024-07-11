import sklearn
from sklearn.ensemble import RandomForestClassifier

class EdgeMachineLearning:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.model = RandomForestClassifier(n_estimators=100)

    def train_model(self):
        self.model.fit(self.X, self.y)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate_model(self):
        return self.model.score(self.X, self.y)
