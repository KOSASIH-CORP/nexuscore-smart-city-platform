#include <iostream>
#include <vector>

class EnergyManagementSystem {
private:
    std::vector<Building> buildings;

public:
    EnergyManagementSystem() {}

    void addBuilding(Building building) {
        buildings.push_back(building);
    }

    void optimizeEnergyUsage() {
        for (Building building : buildings) {
            building.optimizeEnergyUsage();
        }
    }

    void displayEnergyUsage() {
        for (Building building : buildings) {
            building.displayEnergyUsage();
        }
    }
};

class Building {
private:
    std::string id;
    double energyUsage;

public:
    Building(std::string id, double energyUsage) {
        this->id = id;
        this->energyUsage = energyUsage;
    }

    void optimizeEnergyUsage() {
        // Optimize energy usage using machine learning algorithms
    }

    void displayEnergyUsage() {
        std::cout << "Building " << id << " energy usage: " << energyUsage << std::endl;
    }
};
