import qiskit

class QuantumKeyDistribution:
    def __init__(self, alice_qubit, bob_qubit):
        self.alice_qubit = alice_qubit
        self.bob_qubit = bob_qubit

    def generate_key(self):
        alice_measurement = self.alice_qubit.measure()
        bob_measurement = self.bob_qubit.measure()
        if alice_measurement == bob_measurement:
            return alice_measurement
        return None
