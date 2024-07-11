from flask import Blueprint, request, jsonify
from models.patient_model import PatientModel

patient_blueprint = Blueprint('patient', __name__)

@patient_blueprint.route('/patient/data', methods=['GET'])
def get_patient_data():
    patient_model = PatientModel()
    data = patient_model.predict([[1, 2, 3]])  # dummy data
    return jsonify({'data': data})

@patient_blueprint.route('/patient/train', methods=['POST'])
def train_patient_model():
    patient_model = PatientModel()
    data = request.get_json()
    patient_model.train(data['X'], data['y'])
    return jsonify({'message': 'Model trained successfully'})
