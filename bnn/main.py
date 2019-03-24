import numpy as np
from neuralnet import NN
if __name__ == "__main__":
    nn = NN(2,1,1)
    X = np.array([1,2])
    y = nn.feed(X)
    print(nn.output_layer.activities)