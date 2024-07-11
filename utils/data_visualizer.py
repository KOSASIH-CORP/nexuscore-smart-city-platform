import matplotlib.pyplot as plt
import numpy as np

class DataVisualizer:
    def __init__(self):
        pass

    def visualize(self, data):
        plt.plot(np.arange(len(data)), data)
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.title("Data Visualization")
        plt.show()

    def visualize_multiple(self, data_list):
        for i, data in enumerate(data_list):
            plt.subplot(len(data_list), 1, i+1)
            plt.plot(np.arange(len(data)), data)
            plt.xlabel("Time")
            plt.ylabel("Value")
            plt.title(f"Data Visualization {i+1}")
        plt.tight_layout()
        plt.show()
