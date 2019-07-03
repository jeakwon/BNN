from base import Base
import numpy as np
import random

# Settings
random.seed(0)
np.set_printoptions(2)
def sigmoid(x, derivative=False):
    sigm = 1. / (1. + np.exp(-x))
    if derivative:
        return sigm * (1. - sigm)
    return sigm

class NeuralNet(Base):
    def __init__(self, ID=None, struct=()):
        self.ID = ID
        self.neuron_layers = None
        self.synapse_layers = None
        self.build(struct)

    def feed(self, x, y):
        if self.struct[0] != len(x):
            raise Exception('x data length does not match with input layer neuron numbers')
        if self.struct[-1] != len(y):
            raise Exception('y data length does not match with input layer neuron numbers')
        self.x = x
        self.y = y

    def predict(self, x):
        self.x = x
        return self.ffrs[-1]


    @property
    def ffrs(self): 
        return [layer.ffrs for layer in self.neuron_layers]
    @property
    def rfrs(self): 
        return [layer.rfrs for layer in self.neuron_layers]
    @property
    def dfrs(self): 
        return [layer.rfrs-layer.ffrs for layer in self.neuron_layers]

    def build(self, struct):
        # Reset layers
        self.struct = struct
        self.neuron_layers = []
        self.synapse_layers = []
        
        # build neuron layers
        for layer_id, num_neurons in enumerate(struct):
            neuron_layer = NeuronLayer(ID=layer_id, neural_net=self, num_neurons=num_neurons)
            self.neuron_layers.append(neuron_layer)

        # build synapse layers
        for layer_id, (upper_neuron_layer, lower_neuron_layer) in enumerate(zip(self.neuron_layers[:-1], self.neuron_layers[1:])):
            synapse_layer = SynapseLayer(ID=layer_id, neural_net=self, 
                upper_neuron_layer=upper_neuron_layer, lower_neuron_layer=lower_neuron_layer)
            self.synapse_layers.append(synapse_layer)

    @property
    def ws(self):
        return [layer.ws for layer in self.synapse_layers]
    
    def ws_stdp(self):
        for layer in self.synapse_layers:
            layer.ws_stdp()

    def view(self, decimal=2):
        # if decimal != None:
            # np.set_printoptions(decimal)
        # from pprint import pprint
        for layer in self.neuron_layers:
            print(f'{layer}:{layer.neurons}')
            # print(f'{layer}:\n{layer.frs}')
            
        for layer in self.synapse_layers:
            print(f'{layer}:{layer.synapses}')
            # print(f'{layer}:\n{layer.ws}')
        

class NeuronLayer(Base):
    def __init__(self, ID=None, neural_net=None, num_neurons=0):
        self.ID = ID
        self.neural_net = neural_net
        self.neurons = None
        self.create(num_neurons)
    
    def create(self, num_neurons):
        self.neurons = [Neuron(ID=neuron_id, neuron_layer=self) for neuron_id in range(num_neurons)]

    @property
    def ffrs(self):
        if self.neurons:
            return np.matrix([neuron.ffr for neuron in self.neurons])
        return None

    @property
    def rfrs(self):
        if self.neurons:
            return np.matrix([neuron.rfr for neuron in self.neurons])
        return None

    @property
    def dfrs(self):
        if self.neurons:
            return np.matrix([neuron.dfr for neuron in self.neurons])
        return None

class SynapseLayer(Base):
    def __init__(self, ID=None, neural_net=None, upper_neuron_layer=None, lower_neuron_layer=None):
        self.ID = ID
        self.neurla_net = neural_net
        self.synapses = None
        self.create(upper_neuron_layer, lower_neuron_layer)

    def create(self, upper_neuron_layer, lower_neuron_layer):
        rows, cols = upper_neuron_layer.neurons, lower_neuron_layer.neurons
        self.synapses = [[Synapse(ID=(row.ID, col.ID), synapse_layer=self, pre=row, post=col) for col in cols] for row in rows]

    @property
    def ws(self):
        if self.synapses:
            return np.matrix([[synapse.w for synapse in row ] for row in self.synapses])
        return None

    def ws_stdp(self):
        if self.synapses:
            for row in self.synapses:
                for synapse in row:
                    synapse.stdp()

class Neuron(Base):
    def __init__(self, ID=None, neuron_layer=None):
        self.ID = ID
        self.neuron_layer = neuron_layer
        self.dendrite = []
        self.axon = []
        self.th = 0 #random.random()

    @property
    def ffr(self):
        ffr = 0
        if not self.dendrite:
            ffr = self.neuron_layer.neural_net.x[self.ID]
        for synapse in self.dendrite:
            ffr += synapse.pre.ffr * synapse.w-synapse.pre.th
        return np.tanh(ffr)

    @property
    def rfr(self):
        rfr = 0
        if not self.axon:
            rfr = self.neuron_layer.neural_net.y[self.ID]
        for synapse in self.axon:
            rfr += synapse.post.rfr * synapse.w-synapse.post.th
        return np.tanh(rfr)

    @property
    def dfr(self):
        return self.rfr-self.ffr

class Synapse(Base):
    def __init__(self, ID=None, synapse_layer=None, pre=None, post=None):
        self.ID = ID
        self.synapse_layer = synapse_layer
        self.pre = pre
        if self.pre:
            self.pre.axon.append(self)
        self.post = post
        if self.post:
            self.post.dendrite.append(self)
        self.post = post
        self.w = random.random()

    def stdp(self):
        self.w = self.w*2**-(self.pre.dfr-self.post.dfr)
        return self.w


if __name__ == "__main__":
    # nn = NeuralNet(struct=(3,4,2))
    # print(nn.synapse_layers[0])

    X=[
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ]
    Y=[[0],[1],[1],[0]]

    nn = NeuralNet(struct=(2,3,3,21))

    for i in range(1000):
        for x, y in zip(X,Y):
            nn.feed(x=x, y=y)
            nn.ws_stdp()
            print(nn.rfrs[0], nn.ffrs[-1], )
    print(nn.predict([0,0]))
    print(nn.predict([0,1]))
    print(nn.predict([1,0]))
    print(nn.predict([1,1]))