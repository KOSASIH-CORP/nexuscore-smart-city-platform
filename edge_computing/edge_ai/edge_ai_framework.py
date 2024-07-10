import tensorflow as tf

class EdgeAIFramework:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = tf.keras.models.load_model(self.model_path)

    def inference(self, input_data):
        return self.model.predict(input_data)

    def update_model(self, new_model_path):
        self.model = tf.keras.models.load_model(new_model_path)
