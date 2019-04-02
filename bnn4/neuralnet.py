from neuron import Neuron
from synapse import Synapse

class NN:
    def __init__(self,*neurons):
        """
            :: examples

                nn = NN(2,3,4)
                nn.neuron_layers
                nn.synapse_layers
                nn.neuron(0, 1) or nn.neuron(neuron_layer=0, ID=1)
                nn.synapes(0, 1, 2) or nn.synapes(synapse_layer=0, pre_ID=1, post_ID=2)
        """
        self.struct         = neurons
        self.neuron_layers  = self._get_neuron_layers()
        self.synapse_layers = self._get_synapse_layers()

    def neuron(self, layer, ID):
        return self.neuron_layers[layer][ID]

    def synapse(self, layer, pre_ID, post_ID):
        return self.synapse_layers[layer][pre_ID][post_ID]

    def _get_neuron_layers(self):
        neuron_layers = [[Neuron(neuron_layer, ID, self) for ID in range(i)] for neuron_layer, i in enumerate(self.struct)]
        return neuron_layers

    def _get_synapse_layers(self):
        synapse_layers = []
        for synapse_layer, shape in enumerate(zip(self.struct[:-1], self.struct[1:])):
            matrix = [[Synapse(synapse_layer, pre_ID, post_ID, self) for post_ID in range(shape[1])] for pre_ID in range(shape[0])]
            synapse_layers.append(matrix)
        return synapse_layers

if __name__ == "__main__":
    from pprint import pprint
    nn = NN(2,3,4)
    pprint(nn.neuron_layers[0])
    pprint(nn.synapse_layers)
    print(nn.synapse(0,1,2).w)
    print(nn.neuron(0,1).fr)