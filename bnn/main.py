import numpy as np
from neuralnet import NN
from pprint import pprint
if __name__ == "__main__":
    nn = NN(5,5,2)
    X = np.array([0.5,0.6,0.7,0.8,0.9])
    nn.feed(X)
    pprint(nn.receptors)
    nn.feed(X)
    pprint(nn.receptors)
    nn.feed(X)
    pprint(nn.receptors)
    nn.feed(X)
    pprint(nn.receptors)
    print(nn.activities)