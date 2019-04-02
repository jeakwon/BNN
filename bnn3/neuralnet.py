import numpy as np
from layer import Layer

class NN:
    """
        ::

            nn = NeuralNet(2,3,2)
            nn.layers
            nn.layer(1)
    """
    def __init__(self, *neurons:int):
        self.shape              = neurons
        self.input_layer_ID     = 0
        self.output_layer_ID    = len(neurons)-1
        self.layers             = self._get_layers()
        self.synapses           = self._get_synapses()

    def layer(self,ID):
        return self.layers[ID]

    def _get_layers(self):
        layers = list()
        for layer_id, n_neurons in enumerate(self.shape):
            layers.append(Layer(nn=self, ID=layer_id, n_neurons=n_neurons))
        return layers

    def synapse(self, ID):
        for synapse in self.synapses:
            if synapse.ID == ID:
                return synapse

    def _get_synapeses(self):
        synapses = list()
        for layer in self.layers:
            for neuron in layer.neurons:
                for lower_neuron in neuron.lower_neurons:
                    synapses.append(neuron.project(lower_neuron))
        return synapses

    def __str__(self):
        return 'NeuralNet{}'.format(self.shape)

    def __repr__(self):
        return 'NeuralNet{}'.format(self.shape)