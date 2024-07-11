require "sinatra"
require "json"

class EnergyManagementDashboard < Sinatra::Base
  get "/energy_management" do
    energy_consumptions = EnergyConsumption.all
    erb :energy_management, locals: { energy_consumptions: energy_consumptions }
  end

  post "/energy_management" do
    data = JSON.parse(request.body.read)
    energy_consumption = EnergyConsumption.create!(timestamp: data["timestamp"], energy_consumption: data["energy_consumption"])
    redirect "/energy_management"
  end
end
