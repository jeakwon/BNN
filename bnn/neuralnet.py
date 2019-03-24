from layer import Layer

class NN:
    def __init__(self,*neurons:int):
        """
            ::

                nn = NeuralNet(2,3,2)
                nn.layers
                nn.layer(1)
        """
        self.struct = neurons
        self.layers = self._get_layers()

    def _get_layers(self):
        layers = dict()
        for layer_id, n_neurons in enumerate(self.struct):
            layers[layer_id] = Layer(nn=self, ID=layer_id, n_neurons=n_neurons)
        return layers
    
    def layer(self,ID):
        return self.layers[ID]

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

    def __str__(self):
        return 'NeuralNet{}'.format(self.struct)

    def __repr__(self):
        return 'NeuralNet{}'.format(self.struct)
