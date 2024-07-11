from flask import Blueprint, request, jsonify
from models.health_model import HealthModel

health_blueprint = Blueprint('health', __name__)

@health_blueprint.route('/health/data', methods=['GET'])
def get_health_data():
    health_model = HealthModel()
    data = health_model.predict([[1, 2, 3]])  # dummy data
    return jsonify({'data': data})

@health_blueprint.route('/health/train', methods=['POST'])
def train_health_model():
    health_model = HealthModel()
    data = request.get_json()
    health_model.train(data['X'], data['y'])
    return jsonify({'message': 'Model trained successfully'})
