import pandas as pd

class DataAggregator:
    def __init__(self):
        pass

    def aggregate(self, data_list):
        df = pd.DataFrame(data_list)
        aggregated_data = df.groupby("device_id").mean()
        return aggregated_data

    def visualize(self, aggregated_data):
aggregated_data.plot(kind="bar")
        plt.xlabel("Device ID")
        plt.ylabel("Aggregated Data")
        plt.title("Data Aggregation")
        plt.show()
