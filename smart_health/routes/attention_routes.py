from flask import Blueprint, request, jsonify
from models.attention_model import AttentionModel

attention_blueprint = Blueprint('attention', __name__)

@attention_blueprint.route('/attention', methods=['POST'])
def predict_attention():
    attention_model = AttentionModel(input_dim=128, hidden_dim=256, output_dim=128)
    input_seq = request.get_json()['input_seq']
    output = attention_model(input_seq)
    return jsonify({'output': output})

@attention_blueprint.route('/train', methods=['POST'])
def train_attention():
    attention_model = AttentionModel(input_dim=128, hidden_dim=256, output_dim=128)
    input_seq = request.get_json()['input_seq']
    output = request.get_json()['output']
    criterion = nn.MSELoss()
    optimizer = optim.Adam(attention_model.parameters(), lr=0.001)
    for epoch in range(10):
        optimizer.zero_grad()
        output_pred = attention_model(input_seq)
        loss = criterion(output_pred, output)
        loss.backward()
        optimizer.step()
    return jsonify({'message': 'Model trained successfully'})
