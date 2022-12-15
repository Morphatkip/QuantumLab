

def bob(qc_ab):
    ##BOB CHOOSES
    #Alice sends the qubit sequence to Bob, and Bob randomly chooses measurements
    qc_ab.h(0) # or qc.z(0) # switch these based on your own choice
    qc_ab.z(1) # or qc.h(1)
    qc_ab.z(2) # or qc.z(2)
    qc_ab.h(3) # or qc.z(3)
    qc_ab.z(4) # or qc.h(4)
    qc_ab.h(5) # or qc.h(5)
    qc_ab.barrier()
    print("============================================================================")
    print("Bob receives sequence from Alice chooses and chooses  random measurement")
    print(qc_ab)
    print("============================================================================")
    print()