from synapse import Synapse
class Neuron:
    def __init__(self, nn=None, layer=None,ID=None):
        self.nn         = nn
        self.layer      = layer
        self.ID         = ID

    def project(self, to):
        return Synapse(self,to)


    @property
    def upper_neurons(self):
        if self.layer.ID is self.nn.input_layer_ID:
            return []
        else:
            upper_layer = self.nn.layer(self.layer.ID-1)
            return upper_layer.neurons

    @property
    def lower_neurons(self):
        if self.layer.ID is self.nn.output_layer_ID:
            return []
        else:
            lower_layer = self.nn.layer(self.layer.ID+1)
            return lower_layer.neurons

    


    def __str__(self):
        return 'Neuron({})'.format(self.ID)

    def __repr__(self):
        return 'Neuron({})'.format(self.ID)
