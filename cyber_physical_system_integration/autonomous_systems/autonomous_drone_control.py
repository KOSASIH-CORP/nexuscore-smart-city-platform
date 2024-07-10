import dronekit

class AutonomousDroneControl:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def takeoff(self, altitude):
        self.vehicle.arm()
        self.vehicle.takeoff(altitude)

    def land(self):
        self.vehicle.land()

    def set_velocity(self, velocity):
        self.vehicle.send_global_velocity(velocity)
