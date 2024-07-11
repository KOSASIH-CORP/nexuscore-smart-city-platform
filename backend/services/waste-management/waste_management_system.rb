class WasteManagementSystem
  def initialize
    @waste_bins = []
  end

  def add_waste_bin(waste_bin)
    @waste_bins << waste_bin
  end

  def optimize_waste_collection
    @waste_bins.each do |waste_bin|
      waste_bin.optimize_collection
    end
  end

  def display_waste_levels
    @waste_bins.each do |waste_bin|
      waste_bin.display_level
    end
  end
end

class WasteBin
  attr_accessor :id, :level

  def initialize(id, level)
    @id = id
    @level = level
  end

  def optimize_collection
    # Optimize waste collection using genetic algorithms
  end

  def display_level
    puts "Waste bin #{@id} level: #{@level}%"
  end
end
