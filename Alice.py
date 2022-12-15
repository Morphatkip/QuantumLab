from Encrypt import encrypt
def alice(qc_ab, message):
    data = message.encode('ASCII')
    ##ENCODE BIT STRING
    #The random bit sequence Alice needs to encode is: 100100,
    # so the first and fourth qubits are flipped from |0> -> |1>
    print("============================================================================")
    print("Alice (polling station) station sends the key to Bob(Tallying centre")
    print("============================================================================")
    print()
    qc_ab.x(0) #The first qubit is indexed at 0, following Python being zero-indexed. From now on it'll be referred to as qubit 0 and so on.
    qc_ab.x(3)  
    qc_ab.barrier() 


    ##ALICE CHOOSES
    #Alice randomly chooses to apply an X or an H.  
    #Note that since the state is already either a |0> or |1>, a Z essentially leaves the qubit state unchanged. But let's write it anyway, shall we? 
    
    qc_ab.h(0) # or qc.z(0) # switch these based on your own choice
    qc_ab.z(1) # or qc.h(1)
    qc_ab.z(2) # or qc.h(2)
    qc_ab.h(3) # or qc.z(3)
    qc_ab.z(4) # or qc.h(4)
    qc_ab.h(5) # or qc.z(5)
    qc_ab.barrier()
    print("============================================================================")
    print("Allice choses  random  values and sends it to Bob")
    print(qc_ab)
    print("============================================================================")
    print()

    #alice encrypts election result that he wants to send
    ciphertext, tag, nonce = encrypt(b'0000000000100100',data)
    print("============================================================================")
    print("encrypted message:" , ciphertext)
    print("============================================================================")
    print()
    return ciphertext, tag, nonce

    
    


