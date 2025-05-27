
def run_qiskit_gpu_example():
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import numpy as np

def run_qgpu_bell_test(num_qubits=2, shots=2048):
    print(f"Building a Bell state circuit with {num_qubits} qubits...")
    qc = QuantumCircuit(num_qubits, num_qubits)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure(range(num_qubits), range(num_qubits))

    backend = Aer.get_backend('qasm_simulator')
    transpiled = transpile(qc, backend, optimization_level=3)
    print("Running simulation on Aer qasm_simulator (GPU if available)...")
    job = backend.run(transpiled, shots=shots)
    result = job.result()
    counts = result.get_counts()
    print(f"Simulation results: {counts}")

    # Efficient plotting
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    # Histogram (Qiskit style)
    plot_histogram(counts, ax=axs[0])
    axs[0].set_title("Qiskit Histogram")

    # Pie chart
    labels = list(counts.keys())
    sizes = list(counts.values())
    axs[1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    axs[1].set_title("Pie Chart")
    axs[1].axis('equal')

    # Bar chart
    axs[2].bar(labels, sizes, color='skyblue')
    axs[2].set_xlabel('Bitstring')
    axs[2].set_ylabel('Counts')
    axs[2].set_title('Bar Chart')

    plt.suptitle(f"QGPU Bell State Simulation Results ({shots} shots)")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    print("QGPU (Quantum GPU) Bell state test with Qiskit Aer - Python")
    run_qgpu_bell_test()
    print("Test finished.")

if __name__ == "__main__":
    print("QGPU (Quantum GPU) test with Qiskit - Python")
    run_qiskit_gpu_example()
    print("Test finished.")
