import axios from "axios";

class EnergyManagementController {
  async getEnergyConsumption() {
    const response = await axios.get("https://api.nexuscore-smart-city-platform.com/energy_consumption");
    return response.data;
  }

  async createEnergyConsumption(data) {
    const response = await axios.post("https://api.nexuscore-smart-city-platform.com/energy_consumption", data);
    return response.data;
  }
}

export default EnergyManagementController;
