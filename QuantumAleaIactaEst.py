import numpy as np
from qiskit import(QuantumCircuit, execute, Aer)
from qiskit.visualization import plot_histogram
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<html>
    <head>
        <title>Quantum Alea Iacta Est!</title>
    </head>
    <body>
        <h1 style="font-size:30vw;text-align:center;color:SpringGreen;margin:10px">''' + str(int(dice(), 2)) + '''</h1>
        <h1 style="font-size:5vw;text-align:center;color:SkyBlue;">Press refresh to cast again!</h1>
    </body>
</html>'''

def bit_from_counts(counts):
    return [k for k, v in counts.items() if v == 1][0]

def dice():
    bits = ''
    # Use Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')

    while True:
        for x in range(3):
            # Create a Quantum Circuit acting on the q register
            circuit = QuantumCircuit(2, 2)

            # Add a H gate on qubit 0
            circuit.h(0)

            # Add a CX (CNOT) gate on control qubit 0 and target qubit 1
            circuit.cx(0, 1)

            # Map the quantum measurement to the classical bits
            circuit.measure([0,1], [0,1])

            # Execute the circuit on the qasm simulator
            job = execute(circuit, simulator, shots=1)

            # Grab results from the job
            result = job.result()
            counts = result.get_counts(circuit)
            if bit_from_counts(counts) == '11':
                bits += '1'
            elif bit_from_counts(counts) == '00':
                bits += '0'
            else:
                print('Quantum inaccuracy!')
        
        if bits == '111' or bits == '000':
            bits = ''
        else:
            return bits
d=dice()
print("bitit o: ", d)
print("noppa o: ", int(d, 2))
print('strinkinä: ', str(int(d, 2)))

if __name__ == '__main__':
    app.config['DEBUG']=True
    app.run(threaded=True, port=5000)
'''
# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit
circuit.draw()'''