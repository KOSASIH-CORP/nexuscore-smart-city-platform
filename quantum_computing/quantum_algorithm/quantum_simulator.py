import qiskit

class QuantumSimulator:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = qiskit.QuantumCircuit(num_qubits)

    def add_gate(self, gate, qubit):
        self.circuit.append(gate, [qubit])

    def run_simulation(self):
        job = qiskit.execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        return result.get_counts()
