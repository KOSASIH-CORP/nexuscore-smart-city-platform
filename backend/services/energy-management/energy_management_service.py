import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

class EnergyConsumption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    energy_consumption = db.Column(db.Float, nullable=False)

@app.route("/energy_consumption", methods=["GET"])
def get_energy_consumption():
    energy_consumptions = EnergyConsumption.query.all()
    return jsonify([{"id": ec.id, "timestamp": ec.timestamp, "energy_consumption": ec.energy_consumption} for ec in energy_consumptions])

@app.route("/energy_consumption", methods=["POST"])
def create_energy_consumption():
    data = request.get_json()
    energy_consumption = EnergyConsumption(timestamp=data["timestamp"], energy_consumption=data["energy_consumption"])
    db.session.add(energy_consumption)
    db.session.commit()
    return jsonify({"id": energy_consumption.id})

if __name__ == "__main__":
    app.run(debug=True)
