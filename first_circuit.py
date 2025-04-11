from qiskit import QuantumCircuit, transpile, visualization
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from qiskit.visualization import plot_state_qsphere
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_city
# Create a quantum circuit with 5 qubits and 5 classical bits for a more complex example
circuit = QuantumCircuit(5, 5)

# Create a Bell pair between qubits 0 and 1
# Create a Bell pair between qubits 0 and 1
circuit.h(0)  # Hadamard on qubit 0
circuit.cx(0, 1)  # CNOT with qubit 0 as control and qubit 1 as target

# Create GHZ state by extending entanglement to all qubits
circuit.cx(1, 2)
circuit.cx(2, 3)
circuit.cx(3, 4)

# Apply single-qubit gates
circuit.x(2)  # X gate on qubit 2
circuit.h(2)  # Hadamard on qubit 2
circuit.t(0)  # T gate on qubit 0
circuit.tdg(1)  # T-dagger gate on qubit 1
circuit.s(2)  # S gate on qubit 2

# Additional entangling operations
circuit.cx(1, 2)  # CNOT with qubit 1 as control and qubit 2 as target
circuit.cx(2, 3)
circuit.cx(3, 4)
circuit.cx(4, 0)  # Creates a cycle in the entanglement


# Measure all qubits
circuit.barrier()  # Add a barrier for visual separation
circuit.measure([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])

# Simulate the circuit with more shots for better statistics
simulator = AerSimulator()
compiled_circuit = transpile(circuit, simulator, optimization_level=1) 
result = simulator.run(compiled_circuit, shots=32768 ).result()
counts = result.get_counts()

print("Measurement results:")
for outcome, count in counts.items():
    probability = count / 32768 
    print(f"|{outcome}⟩: {count} counts ({probability:.2%})")

# Visualize the results with a histogram
fig, ax = plt.subplots(figsize=(12, 6))
visualization.plot_histogram(counts, bar_labels=True, color='teal', title="Quantum Circuit Results")
plt.savefig('quantum_results.png', dpi=300, bbox_inches='tight')

# Visualize the results with a q-sphere
# Create a copy of the circuit without measurements for statevector simulation
circuit_no_measure = QuantumCircuit(5)

# Create a Bell pair between qubits 0 and 1
circuit_no_measure.h(0)
circuit_no_measure.cx(0, 1)

# Create GHZ state by extending entanglement
circuit_no_measure.cx(1, 2)
circuit_no_measure.cx(2, 3)
circuit_no_measure.cx(3, 4)

# Apply single-qubit gates
circuit_no_measure.x(2)
circuit_no_measure.h(2)
circuit_no_measure.t(0)
circuit_no_measure.tdg(1)
circuit_no_measure.s(2)

# Additional entangling operations
circuit_no_measure.cx(1, 2)
circuit_no_measure.cx(2, 3)
circuit_no_measure.cx(3, 4)
circuit_no_measure.cx(4, 0)  # Creates a cycle in the entanglement

# Get the statevector directly
statevector = Statevector.from_instruction(circuit_no_measure)

# Plot the q-sphere representation
fig_qsphere = plt.figure(figsize=(10, 10))
plot_state_qsphere(statevector)
plt.title("Q-sphere Representation of Quantum State")
plt.savefig('qsphere_visualization.png', dpi=300, bbox_inches='tight')

# Draw the circuit
print(circuit.draw(output='text'))  # Quick check
circuit.draw(output='mpl', filename='advanced_circuit.png', style={'fontsize': 12})
plot_state_city(statevector, title="5-Qubit State City Plot")
plt.savefig('state_city.png')

# print("Circuit visualization, q-sphere, and results saved as PNG files!")

