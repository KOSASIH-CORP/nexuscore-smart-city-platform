import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///iot.db"
db = SQLAlchemy(app)

class IoTDevice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(100), unique=True, nullable=False)
    device_type = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(200), nullable=False)

@app.route("/devices", methods=["GET"])
def get_devices():
    devices = IoTDevice.query.all()
    return jsonify([{"id": device.id, "device_id": device.device_id, "device_type": device.device_type} for device in devices])

@app.route("/devices/<device_id>", methods=["GET"])
def get_device(device_id):
    device = IoTDevice.query.filter_by(device_id=device_id).first()
    if device:
        return jsonify({"id": device.id, "device_id": device.device_id, "device_type": device.device_type, "data": device.data})
    else:
        return jsonify({"error": "Device not found"}), 404

@app.route("/devices", methods=["POST"])
def create_device():
    data = request.get_json()
    device = IoTDevice(device_id=data["device_id"], device_type=data["device_type"], data=data["data"])
    db.session.add(device)
    db.session.commit()
    return jsonify({"id": device.id, "device_id": device.device_id, "device_type": device.device_type, "data": device.data})

if __name__ == "__main__":
    app.run(debug=True)
