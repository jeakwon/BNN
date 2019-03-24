import numpy as np
from neuron import Neuron

class Layer:
    def __init__(self, nn=None, ID=None, n_neurons=0):
        self.nn         = nn
        self.ID         = ID
        self.n_neurons  = n_neurons
        self.neurons    = self._get_neurons()

    def neuron(self,ID):
        return self.neurons[ID]

    def _get_neurons(self):
        neurons = dict()
        for n in range(self.n_neurons):
            neurons[n] = Neuron(nn=self.nn, layer=self,ID=n)
        return neurons

    @property
    def activities(self):
        return self._get_activities()

    def _get_activities(self):
        activities = []
        for n in range(self.n_neurons):
            activities.append(self.neuron(n).activity)
        return np.array(activities)

    @property
    def upper(self):
        return self._get_upper_layer()

    def _get_upper_layer(self):
        current_layer_ID = self.ID
        if current_layer_ID is self.nn.input_layer_ID:
            return None
        upper_layer_ID = self.ID - 1 
        return self.nn.layer(upper_layer_ID)

    @property
    def lower(self):
        return self._get_lower_layer()

    def _get_lower_layer(self):
        current_layer_ID = self.ID
        if current_layer_ID is self.nn.output_layer_ID:
            return None
        lower_layer_ID = self.ID + 1
        return self.nn.layer(lower_layer_ID)

    @property
    def info(self):
        return 'nn:{}, this:{}'.format(self.nn, self)

    def __str__(self):
        return 'Layer({})'.format(self.ID)

    def __repr__(self):
        return 'Layer({})'.format(self.ID)
