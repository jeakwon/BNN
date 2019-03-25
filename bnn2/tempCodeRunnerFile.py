    s00_10.fit()
    s01_10.fit()
    print('{:.2f} {:.2f} : Input Neurons\n{:.2f} {:.2f} : Synapses\n  {:.2f}    : Output Neuron'.format(
        n00.fr,n01.fr,s00_10.w,s01_10.w,n10.fr))