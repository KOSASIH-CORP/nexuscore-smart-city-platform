import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class Analytics:
    def __init__(self, data):
        self.data = data

    def train_model(self):
        X = self.data.drop(["target"], axis=1)
        y = self.data["target"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model

    def make_prediction(self, model, data):
        return model.predict(data)

analytics = Analytics(pd.read_csv("data.csv"))
model = analytics.train_model()
prediction = analytics.make_prediction(model, pd.read_csv("new_data.csv"))
print(prediction)
