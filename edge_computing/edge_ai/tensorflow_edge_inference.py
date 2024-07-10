import tensorflow as tf

class TensorFlowEdgeInference:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = tf.keras.models.load_model(self.model_path)

    def inference(self, input_data):
        output = self.model.predict(input_data)
        return output
