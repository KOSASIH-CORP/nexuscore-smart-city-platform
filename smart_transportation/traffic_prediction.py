import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class TrafficPrediction:
    def __init__(self, traffic_data):
        self.traffic_data = traffic_data
        self.model = self.create_model()
    
    def create_model(self):
        # Create traffic prediction model using random forest regressor
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        return model
    
    def train_model(self):
        # Train traffic prediction model using training data
        X = self.traffic_data.drop('traffic_volume', axis=1)
        y = self.traffic_data['traffic_volume']
        self.model.fit(X, y)
    
    def predict_traffic(self, new_data):
        # Predict traffic volume using trained model
        prediction = self.model.predict(new_data)
        return prediction
    
    def evaluate_performance(self, test_data):
        # Evaluate performance of traffic prediction model
        X = test_data.drop('traffic_volume', axis=1)
        y = test_data['traffic_volume']
        prediction = self.model.predict(X)
        mse = mean_squared_error(y, prediction)
        return mse
