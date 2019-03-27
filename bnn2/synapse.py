import numpy as np
WEIGHT = np.random.random()
DELTA_WEIGHT = 0.5+1.5*(np.random.random())

class Synapse:
    def __init__(self):
        self.w = WEIGHT
        self.dw = DELTA_WEIGHT

    def fit(self):
        self.w = round(np.tanh(self.w*self.dw),3) # using tanh makes weight play around only in 0~1
        
if __name__ == "__main__":
    syn = Synapse()
    for _ in range(100):
        syn.fit()
        print(syn.w,syn.dw)