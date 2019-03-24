class PreSynapse:
    def __init__(self, nn=None, layer=None, neuron=None, ID=None):
        self.nn     = nn
        self.layer  = layer
        self.neuron = neuron
        self.ID     = ID

    @property
    def info(self):
        return 'nn:{}, layer:{}, neuron:{}, this:{}'.format(
            self.nn, self.layer, self.neuron, self)

    @property
    def partner(self):
        return self._get_partner()

    def _get_partner(self):
        neuron_id = self.ID
        postsyn_id = self.neuron.ID
        partner = self.layer.upper.neuron(neuron_id).postsyn(postsyn_id)
        return partner

    def __str__(self):
        return 'PreSynapse({})'.format(self.ID)

    def __repr__(self):
        return 'PreSynapse({})'.format(self.ID)


class PostSynapse:
    def __init__(self, nn=None, layer=None, neuron=None, ID=None):
        self.nn     = nn
        self.layer  = layer
        self.neuron = neuron
        self.ID     = ID
        self.receptor = 1

    @property
    def info(self):
        return 'nn:{}, layer:{}, neuron:{}, this:{}'.format(
            self.nn, self.layer, self.neuron, self)

    @property
    def partner(self):
        return self._get_partner()
        
    def _get_partner(self):
        neuron_id = self.ID
        presyn_id = self.neuron.ID
        partner = self.layer.lower.neuron(neuron_id).presyn(presyn_id)
        return partner

    def __str__(self):
        return 'PostSynapse({})'.format(self.ID)

    def __repr__(self):
        return 'PostSynapse({})'.format(self.ID)