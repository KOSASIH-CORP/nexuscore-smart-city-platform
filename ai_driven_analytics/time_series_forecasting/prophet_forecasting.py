import pandas as pd
from prophet import Prophet

class ProphetForecasting:
    def __init__(self, data, seasonality_mode='additive'):
        self.data = data
        self.model = Prophet(seasonality_mode=seasonality_mode)

    def fit_model(self):
        self.model.fit(self.data)

    def make_forecast(self, periods=30):
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast

    def plot_forecast(self, forecast):
        self.model.plot(forecast)
        plt.show()

    def evaluate_model(self, forecast):
        metrics = self.model.evaluate(forecast)
        return metrics
