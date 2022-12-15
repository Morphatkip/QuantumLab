from qiskit import *
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from Alice import alice
from Bob import bob
from Eve import eve
from Decrypt import decrypt

def key_comparison_process(interception, message):
    qc_ab = QuantumCircuit(6,6) #Create a quantum circuit with 6 qubits and 6 classical bits
    ciphertext, tag, nonce = alice(qc_ab, message)

    if(interception =='1'):
        print('introducing Eve in the network')
        eve(qc_ab)
    bob(qc_ab)
   
    ##PUBLICIZE CHOICES
    #Alice and Bob publicize their choices and only retain those for which their choices match. In this case: qubits 0,1,3,4. 
    #Note: technically Bob performs the measurement BEFORE publicizing, but we're combining the two here since no one is actually communicating.
    qc_ab.measure(0,0)
    qc_ab.measure(1,1)
    qc_ab.measure(3,3)
    qc_ab.measure(4,4)
    print("============================================================================")
    print("Alice and Bob publicize their results and see if there is a match")
    print(qc_ab)
    print("============================================================================")
    print()

    qc_ab.draw(output='mpl') #let's see what this circuit looks like!
    
    plt.show()
    ##EXECUTE
    result = execute(qc_ab, Aer.get_backend('qasm_simulator')).result().get_counts() #We're only making use of the simulator. Refer to [2] to see how you can run this on a real quantum computer.
    
    plot_histogram(result)
    plt.show()
    return result, ciphertext, tag, nonce


if __name__=="__main__":
    print("Eter the polling results to be transmitted to Bob")
    message = input()
    while True:
        print('Choose Option to simulate')
        print('1. Hacker')
        print('2. No hacker')
        interception = input()
        result, ciphertext, tag, nonce= key_comparison_process(interception, message)
        print(result)
        
        # key = b'000000000000'+ result(0)
        if len(result) <= 2:
            key =0
            for x,y in  result.items():
                key = x
          
            key_reverse = key [::-1] 
            key_to_use = '0000000000'+ key_reverse
            key_to_use = key_to_use.encode('ASCII')
            print(key_to_use)
            print("============================================================================")
            print("Decrypting the message .................................")
            print("============================================================================")
            print()
            decryption_results = decrypt( key_to_use,ciphertext, tag, nonce)
            print("decryption results :",decryption_results)
            break 
        else:
         ("Eve is eaves dropping process will begin")

        