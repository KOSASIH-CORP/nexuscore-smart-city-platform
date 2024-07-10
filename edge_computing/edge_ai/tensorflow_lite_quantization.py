import tensorflow as tf

class TensorFlowLiteQuantization:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = tf.keras.models.load_model(self.model_path)

    def quantize_model(self):
        converter = tf.lite.TFLiteConverter.from_keras_model(self.model)
        tflite_model = converter.convert()
        return tflite_model

    def save_quantized_model(self, tflite_model, output_path):
        with open(output_path, 'wb') as f:
            f.write(tflite_model)
