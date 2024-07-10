import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DataVisualization:
    def __init__(self, data):
        self.data = data
    
    def plot_time_series(self, column):
        # Plot time series data using Matplotlib
        plt.plot(self.data[column])
        plt.xlabel('Time')
        plt.ylabel(column)
        plt.title(f'Time Series of {column}')
        plt.show()
    
    def plot_bar_chart(self, column):
        # Plot bar chart data using Seaborn
        sns.barplot(x=self.data.index, y=self.data[column])
        plt.xlabel('Index')
        plt.ylabel(column)
        plt.title(f'Bar Chart of {column}')
        plt.show()
    
    def plot_heatmap(self, columns):
        # Plot heatmap data using Seaborn
        sns.heatmap(self.data[columns].corr(), annot=True, cmap='coolwarm', square=True)
        plt.xlabel('Features')
        plt.ylabel('Features')
        plt.title('Heatmap of Feature Correlations')
        plt.show()
