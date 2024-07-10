import numpy as np
import tensorflow as tf
from tensorflow import keras

class NeuralNetworkArchitect:
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = self.create_model()
    
    def create_model(self):
        # Create neural network model using Keras
        model = keras.Sequential([
            keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape),
            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Flatten(),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(self.num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model
    
    def train_model(self, training_data, epochs):
        # Train neural network model using training data
        self.model.fit(training_data, epochs=epochs)
    
    def evaluate_model(self, test_data):
        # Evaluate performance of neural network model
        loss, accuracy = self.model.evaluate(test_data)
        return accuracy
    
    def save_model(self, file_path):
        # Save neural network model to file
        self.model.save(file_path)
    
    def load_model(self, file_path):
        # Load neural network model from file
        self.model = keras.models.load_model(file_path)
