from flask import Blueprint, request, jsonify
from models.graph_neural_network import GraphNeuralNetwork

graph_blueprint = Blueprint('graph', __name__)

@graph_blueprint.route('/graph', methods=['POST'])
def predict_graph():
    graph_neural_network = GraphNeuralNetwork(num_layers=3, hidden_dim=128, output_dim=128)
    data = request.get_json()['data']
    data = pyg_data.Data(x=torch.tensor(data['x']), edge_index=torch.tensor(data['edge_index']), batch=torch.tensor(data['batch']))
    output = graph_neural_network(data)
    return jsonify({'output': output})

@graph_blueprint.route('/train', methods=['POST'])
def train_graph():
    graph_neural_network = GraphNeuralNetwork(num_layers=3, hidden_dim=128, output_dim=128)
    data = request.get_json()['data']
    data = pyg_data.Data(x=torch.tensor(data['x']), edge_index=torch.tensor(data['edge_index']), batch=torch.tensor(data['batch']))
    criterion = nn.MSELoss()
    optimizer = optim.Adam(graph_neural_network.parameters(), lr=0.001)
    for epoch in range(10):
        optimizer.zero_grad()
        output = graph_neural_network(data)
        loss = criterion(output, data.y)
        loss.backward()
        optimizer.step()
    return jsonify({'message': 'Model trained successfully'})
