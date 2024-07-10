import qiskit

class QuantumAlgorithm:
    def __init__(self):
        self.quantum_circuit = qiskit.QuantumCircuit(5)

    def add_gate(self, gate_type, qubit_id):
        if gate_type == 'h':
            self.quantum_circuit.h(qubit_id)
        elif gate_type == 'x':
            self.quantum_circuit.x(qubit_id)

    def execute_circuit(self):
        job = qiskit.execute(self.quantum_circuit, backend='qasm_simulator')
        return job.result()
