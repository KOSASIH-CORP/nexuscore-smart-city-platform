import pandas as pd
from prophet import Prophet

class ProphetForecaster:
    def __init__(self, data):
        self.data = data
        self.model = Prophet()

    def fit(self):
        self.model.fit(self.data)

    def forecast(self, periods):
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast
