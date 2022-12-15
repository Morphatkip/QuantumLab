def eve(qc_aeb):
    ##EVE CHOOSES
    qc_aeb.h(0) #play around with these to see how many states with non-zero probabilities show up at the end for a fixed set of Alice's and Bob's choices
    qc_aeb.z(1) 
    qc_aeb.h(2) 
    qc_aeb.h(3) 
    qc_aeb.z(4) 
    qc_aeb.z(5) 
    qc_aeb.barrier()
    print("============================================================================")
    print("Eve intercepts and chooses  random  values ")
    print(qc_aeb)
    print("============================================================================")
    print()
