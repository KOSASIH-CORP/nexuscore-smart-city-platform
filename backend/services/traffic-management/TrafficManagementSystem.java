import java.util.ArrayList;
import java.util.List;

public class TrafficManagementSystem {
    private List<Vehicle> vehicles;
    private List<Road> roads;

    public TrafficManagementSystem() {
        vehicles = new ArrayList<>();
        roads = new ArrayList<>();
    }

    public void addVehicle(Vehicle vehicle) {
        vehicles.add(vehicle);
    }

    public void addRoad(Road road) {
        roads.add(road);
    }

    public void updateTraffic() {
        for (Vehicle vehicle : vehicles) {
            vehicle.updateLocation();
        }

        for (Road road : roads) {
            road.updateTrafficFlow();
        }
    }

    public List<Vehicle> getVehicles() {
        return vehicles;
    }

    public List<Road> getRoads() {
        return roads;
    }
}

class Vehicle {
    private String id;
    private double latitude;
    private double longitude;
    private double speed;

    public Vehicle(String id, double latitude, double longitude, double speed) {
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
        this.speed = speed;
    }

    public void updateLocation() {
        // Update vehicle location using GPS data
    }
}

class Road {
    private String id;
    private double trafficFlow;

    public Road(String id, double trafficFlow) {
        this.id = id;
        this.trafficFlow = trafficFlow;
    }

    public void updateTrafficFlow() {
        // Update traffic flow using sensor data
    }
      }
