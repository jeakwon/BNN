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
        neurons = list()
        for n in range(self.n_neurons):
            neurons.append(Neuron(nn=self.nn, layer=self,ID=n))
        return neurons

    def __str__(self):
        return 'Layer({})'.format(self.ID)

    def __repr__(self):
        return 'Layer({})'.format(self.ID)