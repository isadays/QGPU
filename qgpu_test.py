
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def run_qiskit_gpu_example():
    print("Creating quantum circuit...")
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    print("Transpiling circuit for simulated backend (Aer qasm_simulator)...")
    backend = Aer.get_backend('qasm_simulator')
    transpiled = transpile(qc, backend)
    # Qiskit 2.x: use backend.run instead of execute
    job = backend.run(transpiled, shots=1024)
    result = job.result()
    counts = result.get_counts()
    print(f"Simulation results: {counts}")

    print("Displaying result histogram...")
    fig1 = plot_histogram(counts)
    plt.title("Measurement Results Histogram")
    plt.show()

    # Pie chart
    print("Displaying result pie chart...")
    labels = list(counts.keys())
    sizes = list(counts.values())
    fig2, ax2 = plt.subplots()
    ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Measurement Results Pie Chart")
    plt.show()

    # Bar chart
    print("Displaying result bar chart...")
    fig3, ax3 = plt.subplots()
    ax3.bar(labels, sizes, color='skyblue')
    plt.xlabel('Bitstring')
    plt.ylabel('Counts')
    plt.title('Measurement Results Bar Chart')
    plt.show()

if __name__ == "__main__":
    print("QGPU (Quantum GPU) test with Qiskit - Python")
    run_qiskit_gpu_example()
    print("Test finished.")
