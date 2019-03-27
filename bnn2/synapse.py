import numpy as np

class Synapse:
    def __init__(self):
        self.w = np.random.random()
        self.dw = 0.5+1.5*(np.random.random()) # 0.5~ 2.0 (delta weight)

    def fit(self):
        self.w = np.tanh(self.w*self.dw)
        return self
        
if __name__ == "__main__":
    syn = Synapse()
    for _ in range(10):
        syn.fit()
        print(syn.w,syn.dw)