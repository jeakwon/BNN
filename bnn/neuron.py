from synapse import PreSynapse, PostSynapse

class Neuron:
    def __init__(self, nn=None, layer=None,ID=None):
        self.nn         = nn
        self.layer      = layer
        self.ID         = ID
        self.presyns    = self._get_pre_synapses()
        self.postsyns   = self._get_post_synapses()

    def presyn(self, ID):
        try:
            return self.presyns[ID]
        except:
            raise AttributeError('presyn instance not exist')
    
    def postsyn(self, ID):
        try:
            return self.postsyns[ID]
        except:
            raise AttributeError('postsyn instance not exist')
    
    def _get_pre_synapses(self):
        if self.layer.ID is self.nn.input_layer_ID:
            return None
        upper_layer_ID = self.layer.ID - 1
        n_upper_neurons = self.nn.struct[upper_layer_ID]

        pre_synapses = dict()
        for n in range(n_upper_neurons):
            pre_synapses[n] = PreSynapse(nn=self.nn, layer=self.layer, neuron=self, ID=n)
        return pre_synapses

    def _get_post_synapses(self):
        if self.layer.ID is self.nn.output_layer_ID:
            return None
        lower_layer_ID = self.layer.ID + 1
        n_lower_neurons = self.nn.struct[lower_layer_ID]

        post_synapses = dict()
        for n in range(n_lower_neurons):
            post_synapses[n] = PostSynapse(nn=self.nn, layer=self.layer, neuron=self, ID=n)
        return post_synapses


    @property
    def info(self):
        return 'nn:{}, layer:{}, this:{}'.format(
            self.nn, self.layer, self)

    def __str__(self):
        return 'Neuron({})'.format(self.ID)

    def __repr__(self):
        return 'Neuron({})'.format(self.ID)
