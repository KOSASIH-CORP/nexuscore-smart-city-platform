import carla

class AutonomousVehicleSimulator:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = carla.Client(self.host, self.port)
        self.world = self.client.get_world()

    def spawn_vehicle(self, vehicle_blueprint):
        vehicle = self.world.spawn_actor(vehicle_blueprint, carla.Transform())
        return vehicle

    def destroy_vehicle(self, vehicle):
        vehicle.destroy()

    def set_vehicle_control(self, vehicle, control):
        vehicle.apply_control(control)
