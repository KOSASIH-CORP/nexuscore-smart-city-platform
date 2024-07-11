from flask import Blueprint, request, jsonify
from models.neural_network import NeuralNetwork

predict_blueprint = Blueprint('predict', __name__)

@predict_blueprint.route('/predict', methods=['POST'])
def predict():
    neural_network = NeuralNetwork()
    data = request.get_json()
    X = data['X']
    y = data['y']
    neural_network.train(X,y)
    predictions = neural_network.predict(X)
    return jsonify({'predictions': predictions})

@predict_blueprint.route('/evaluate', methods=['POST'])
def evaluate():
    neural_network = NeuralNetwork()
    data = request.get_json()
    X, y = data['X'], data['y']
    loss, accuracy = neural_network.evaluate(X, y)
    return jsonify({'loss': loss, 'accuracy': accuracy})
