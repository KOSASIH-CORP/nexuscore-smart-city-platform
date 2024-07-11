from flask import Flask, request, jsonify
from routes.health_routes import health_blueprint
from routes.patient_routes import patient_blueprint
from routes.predict_routes import predict_blueprint
from routes.visualization_routes import visualization_blueprint

app = Flask(__name__)

app.register_blueprint(health_blueprint)
app.register_blueprint(patient_routes)
app.register_blueprint(predict_blueprint)
app.register_blueprint(visualization_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
