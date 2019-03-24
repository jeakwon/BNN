import numpy as np
from neuralnet import NN
if __name__ == "__main__":
    nn = NN(5,5,2)
    X = np.array([5,6,7,8,9])
    y = nn.feed(X)
    print(nn.output_layer.activities)
    print(nn.activities)