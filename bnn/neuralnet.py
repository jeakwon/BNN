import numpy as np
from layer import Layer

class NN:
    def __init__(self, *neurons:int):
        """
            ::

                nn = NeuralNet(2,3,2)
                nn.layers
                nn.layer(1)
        """
        self.struct = neurons
        self.layers = self._get_layers()
        self.n_layers = len(neurons)
    
    def feed(self,X):
        self.X = self._input_validation(X)
        # ...
        y = self.output_layer.activities
        return y
    
    def layer(self,ID):
        return self.layers[ID]
    
    @property
    def activities(self):
        activities = dict()
        for n in range(self.n_layers):
            activities[n]= self.layer(n).activities
        return activities

    @property
    def input_layer(self):
        return self.layer(self.input_layer_ID)

    @property
    def output_layer(self):
        return self.layer(self.output_layer_ID)

    @property
    def input_layer_ID(self):
        return 0

    @property
    def output_layer_ID(self):
        return len(self.struct)-1

    @property
    def info(self):
        return 'this:{}'.format(self)

    def _input_validation(self, X):
        if not isinstance(X, np.ndarray):
            raise TypeError('X must be numpy array')
        if X.ndim >1:
            raise ValueError('X must be 1 dimensional array')
        if X.shape[0] is not self.input_layer.n_neurons:
            raise ValueError('X array size must be same with input layer')
        return X

    def _get_layers(self):
        layers = dict()
        for layer_id, n_neurons in enumerate(self.struct):
            layers[layer_id] = Layer(nn=self, ID=layer_id, n_neurons=n_neurons)
        return layers

    def __str__(self):
        return 'NeuralNet{}'.format(self.struct)

    def __repr__(self):
        return 'NeuralNet{}'.format(self.struct)
