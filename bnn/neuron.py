from synapse import PreSynapse, PostSynapse

class Neuron:
    def __init__(self, nn=None, layer=None,ID=None):
        self.nn         = nn
        self.layer      = layer
        self.ID         = ID
        self.presyns    = self._get_pre_synapses()
        self.postsyns   = self._get_post_synapses()
        self.threshold  = 0.3
        self.depressor  = None

    @property
    def activity(self):
        if self.layer is self.nn.input_layer:
            X_input = self.nn.X[self.ID]
            PSP = X_input
        else:
            local_PSP = []
            for n in range(self.layer.upper.n_neurons):
                postsyn_receptors   = self.postsyn(ID=n).receptors
                presyn_ligands      = self.postsyn(ID=n).partner.ligands
                preneuron_activity  = self.postsyn(ID=n).partner.neuron.activity
                local_PSP.append(preneuron_activity * presyn_ligands * postsyn_receptors)
            PSP = sum(local_PSP)
        
        if PSP > self.threshold:
            trigger = PSP-self.threshold
            if trigger > 1:
                activity = 1
                self.depressor = trigger - 1
            else:
                activity = trigger
                self.depressor = None
        else:
            activity = 0
            self.depressor = None
        return activity

    def depress(self):
        if self.depressor is not None:
            local_depressor = self.depressor/len(self.postsyns)+0.01
            for _, postsyn in self.postsyns.items():
                postsyn.receptors -= local_depressor
                if postsyn.receptors < 0:
                    postsyn.receptors = 0

    def presyn(self, ID):
        try:
            return self.presyns[ID]
        except:
            raise NameError('presyn is not exist')
    
    def postsyn(self, ID):
        try:
            return self.postsyns[ID]
        except:
            raise NameError('postsyn is not exist')
    
    def _get_pre_synapses(self):
        if self.layer.ID is self.nn.output_layer_ID:
            return None
        lower_layer_ID = self.layer.ID + 1
        n_lower_neurons = self.nn.struct[lower_layer_ID]

        pre_synapses = dict()
        for n in range(n_lower_neurons):
            pre_synapses[n] = PreSynapse(nn=self.nn, layer=self.layer, neuron=self, ID=n)
        return pre_synapses

    def _get_post_synapses(self):
        if self.layer.ID is self.nn.input_layer_ID:
            return None
        upper_layer_ID = self.layer.ID - 1
        n_upper_neurons = self.nn.struct[upper_layer_ID]

        post_synapses = dict()
        for n in range(n_upper_neurons):
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
