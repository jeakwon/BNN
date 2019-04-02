class Neuron:
    def __init__(self, neuron_layer, ID, nn):
        self.neuron_layer = neuron_layer
        self.ID = ID
        self.nn = nn
        self.fr = 0

    def _calc_fr(self):
        if self.neuron_layer == 0:
            # self.fr = self.nn.input[self.ID]
            pass
        else:
            upper_neurons = self.nn.neuron_layers[self.neuron_layer-1]
            self.ID

    def __repr__(self):
        return 'n({},{})'.format(self.neuron_layer,self.ID)
