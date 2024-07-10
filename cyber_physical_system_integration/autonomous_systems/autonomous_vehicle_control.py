import carla

class AutonomousVehicleControl:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def drive(self, speed, steering_angle):
        self.vehicle.apply_control(carla.VehicleControl(throttle=speed, steer=steering_angle))

    def brake(self):
        self.vehicle.apply_control(carla.VehicleControl(brake=1.0))

    def get_sensor_data(self):
        sensor_data = self.vehicle.get_sensors()
        return sensor_data
