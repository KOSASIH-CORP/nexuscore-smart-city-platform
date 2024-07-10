import numpy as np
from qiskit import QuantumCircuit, execute

class QuantumSimulation:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)
    
    def add_hadamard_gate(self, qubit):
        # Add Hadamard gate to quantum circuit
        self.circuit.h(qubit)
    
    def add_cnot_gate(self, control_qubit, target_qubit):
        # Add CNOT gate to quantum circuit
        self.circuit.cx(control_qubit, target_qubit)
    
    def add_measurement(self, qubit):
        # Add measurement to quantum circuit
        self.circuit.measure(qubit, qubit)
    
    def simulate_circuit(self):
        # Simulate quantum circuit using Qiskit
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        return result
    
    def get_simulation_results(self):
        # Get simulation results
        result = self.simulate_circuit()
        counts = result.get_counts()
        return counts
