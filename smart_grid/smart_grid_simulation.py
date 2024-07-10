import numpy as np
from scipy.optimize import minimize

class SmartGridSimulation:
    def __init__(self, grid_data):
        self.grid_data = grid_data
        self.generators = grid_data['generators']
        self.loads = grid_data['loads']
        self.lines = grid_data['lines']
    
    def simulate_power_flow(self, time_step):
        # Simulate power flow using AC power flow model
        power_flow = np.zeros((len(self.lines),))
        for i in range(len(self.lines)):
            power_flow[i] = self.calculate_power_flow(self.lines[i], time_step)
        return power_flow
    
    def calculate_power_flow(self, line, time_step):
        # Calculate power flow using AC power flow model
        power_flow = line['capacity'] * (1 - line['occupancy'] ** 2)
        return power_flow
    
    def optimize_power_dispatch(self, time_step):
        # Optimize power dispatch using linear programming
        def objective_function(x):
            # Calculate total cost of power dispatch
            cost = np.sum(x * self.generators['cost'])
            return cost
        
        def constraint_function(x):
            # Calculate total power generated
            power_generated = np.sum(x * self.generators['capacity'])
            return power_generated - self.loads['total_load']
        
        bounds = [(0, 1) for _ in range(len(self.generators))]
        res = minimize(objective_function, np.zeros((len(self.generators),)), method="SLSQP", bounds=bounds, constraints={'type': 'ineq', 'fun': constraint_function})
        power_dispatch = res.x
        return power_dispatch
