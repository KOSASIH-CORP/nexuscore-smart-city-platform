from flask import Blueprint, request, jsonify
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

visualization_blueprint = Blueprint('visualization', __name__)

@visualization_blueprint.route('/visualization', methods=['GET'])
def visualize_data():
    data = pd.read_csv('health_data.csv')
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='timestamp', y='heart_rate', data=data)
    plt.title('Heart Rate Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Heart Rate')
    plt.savefig('heart_rate_over_time.png')
    return jsonify({'message': 'Visualization generated successfully'})

@visualization_blueprint.route('/visualization/<string:column>', methods=['GET'])
def visualize_column(column):
    data = pd.read_csv('health_data.csv')
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'{column} Distribution')
    plt.xlabel(column)
    plt.ylabel('Density')
    plt.savefig(f'{column}_distribution.png')
    return jsonify({'message': 'Visualization generated successfully'})
