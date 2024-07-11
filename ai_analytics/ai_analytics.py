import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class AIAnalytics:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train_model(self, data):
        X = data.drop("target", axis=1)
        y = data["target"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, data):
        return self.model.predict(data)

# Load data from IoT framework
data = pd.read_csv("iot_data.csv")

analytics = AIAnalytics()
analytics.train_model(data)

# Make predictions on new data
new_data = pd.DataFrame({"temperature": [20, 30, 40], "humidity": [50, 60, 70]})
predictions = analytics.predict(new_data)
print(predictions)
