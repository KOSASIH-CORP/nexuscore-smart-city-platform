import psutil

class EdgeDeviceMonitoring:
    def __init__(self):
        self.cpu_usage = psutil.cpu_percent()
        self.memory_usage = psutil.virtual_memory().percent

    def get_cpu_usage(self):
        return self.cpu_usage

    def get_memory_usage(self):
        return self.memory_usage
