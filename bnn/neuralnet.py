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
    
    def feed(self, X, depress=True):
        self.X = self._input_validation(X)
        self.y = self.output_layer.activities
        if depress: 
            for _, layer in self.layers.items():
                for _, neuron in layer.neurons.items():
                    neuron.depress()
        return self
    
    def layer(self,ID):
        return self.layers[ID]

    @property
    def neurons(self):
        neurons = dict()
        for layer_ID, layer in self.layers.items():
            for neuron_ID, neuron in layer.neurons.items():
                key = 'L{}N{}'.format(layer_ID, neuron_ID)
                neurons[key] = neuron
        return neurons
    
    @property
    def presyns(self):
        presyns = dict()
        for neuron_ID, neuron in self.neurons.items():
            if neuron.presyns is not None:
                for presyn_ID, presyn in neuron.presyns.items():
                    key = '{}Pr{}'.format(neuron_ID, presyn_ID)
                    presyns[key] = presyn
        return presyns

    @property
    def postsyns(self):
        postsyns = dict()
        for neuron_ID, neuron in self.neurons.items():
            if neuron.postsyns is not None:
                for postsyns_ID, postsyn in neuron.postsyns.items():
                    key = '{}Po{}'.format(neuron_ID, postsyns_ID)
                    postsyns[key] = postsyn
        return postsyns

    @property
    def ligands(self):
        return {k: presyn.ligands for k, presyn in self.presyns.items()}

    @property
    def receptors(self):
        return {k: postsyn.receptors for k, postsyn in self.postsyns.items()}
    
    @property
    def activities(self):
        activities = dict()
        for n in range(self.n_layers):
            activities[n] = self.layer(n).activities
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
