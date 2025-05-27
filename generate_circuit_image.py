from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Save the circuit as an image
circuit_drawer(qc, output='mpl', filename='bell_circuit.png')
