from flask import Blueprint, request, jsonify
from models.transformer_model import TransformerModel

recommendation_blueprint = Blueprint('recommendation', __name__)

@recommendation_blueprint.route('/recommend', methods=['POST'])
def recommend():
    transformer_model = TransformerModel(input_dim=128, hidden_dim=256, output_dim=128, num_heads=8, num_layers=6)
    input_seq = request.get_json()['input_seq']
    output = transformer_model(input_seq)
    return jsonify({'output': output})

@recommendation_blueprint.route('/train', methods=['POST'])
def train():
    transformer_model = TransformerModel(input_dim=128, hidden_dim=256, output_dim=128, num_heads=8, num_layers=6)
    input_seq = request.get_json()['input_seq']
    output = request.get_json()['output']
    criterion = nn.MSELoss()
    optimizer = optim.Adam(transformer_model.parameters(), lr=0.001)
    for epoch in range(10):
        optimizer.zero_grad()
        output_pred = transformer_model(input_seq)
        loss = criterion(output_pred, output)
        loss.backward()
        optimizer.step()
    return jsonify({'message': 'Model trained successfully'})
