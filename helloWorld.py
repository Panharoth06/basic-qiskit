from qiskit import QuantumCircuit;
from qiskit.quantum_info import Pauli;
from qiskit_aer.primitives import Estimator;
import matplotlib.pyplot as plt;

qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)

ZZ = Pauli('ZZ')
ZI = Pauli('ZI')
IZ = Pauli('IZ')
XX = Pauli('XX')
XI = Pauli('XI')
IX = Pauli('IX')

observables = [ZZ, ZI, IZ, XX, XI, IX]

estimator = Estimator()
job = estimator.run([qc] * len(observables), observables)  

data = ['ZZ', 'ZI', 'IZ', 'XX', 'XI', 'IX']
values = job.result().values

plt.bar(data, values)
plt.xlabel('Observable')
plt.ylabel('Expectation Value')
plt.title('Measurement Results')
plt.show()

# Print both the circuit and the measurement results
print("Quantum Circuit:")
print(qc.draw(output='text'))
# print("\nMeasurement Results:")
# print(job.result().values)















