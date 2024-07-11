import tensorflow as tf

class EdgeTransferLearning:
    def __init__(self, base_model, new_classes):
        self.base_model = base_model
        self.new_classes = new_classes

    def fine_tune_model(self, train_data, val_data):
        for layer in self.base_model.layers:
            layer.trainable = False
        x = self.base_model.output
        x = tf.keras.layers.Dense(self.new_classes, activation='softmax')(x)
        self.model = tf.keras.models.Model(inputs=self.base_model.input, outputs=x)
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(train_data, epochs=10, validation_data=val_data)

    def evaluate_model(self, test_data):
        loss, accuracy = self.model.evaluate(test_data)
        return accuracy
