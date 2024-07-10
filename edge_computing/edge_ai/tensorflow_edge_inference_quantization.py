import tensorflow as tf

class TensorFlowEdgeInferenceQuantization:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = tf.keras.models.load_model(self.model_path)

    def quantize_model(self):
        converter = tf.lite.TFLiteConverter.from_keras_model(self.model)
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        tflite_model = converter.convert()
        return tflite_model

    def save_quantized_model(self, tflite_model, output_path):
        with open(output_path, 'wb') as f:
            f.write(tflite_model)

    def load_quantized_model(self, model_path):
        with open(model_path, 'rb') as f:
            tflite_model = f.read()
        return tflite_model

    def inference(self, input_data, tflite_model):
        interpreter = tf.lite.Interpreter(model_content=tflite_model)
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])
        return output_data
