import numpy as np
from random import random

class Neuron:
    def __init__(self,ID:str):
        self.ID         = ID
        self.synapses   = {}

    @property
    def fr(self):
        return self._get_fr()
    
    def _get_fr(self):
        PSPs = list()
        for _, synapse in self.synapses.items():
            if synapse.post is self:
                PSP = round(synapse.pre.fr * synapse.w, 2)
                PSPs.append(PSP)
        return sum(PSPs)
        

    def project_to(self, neuron):
        synapse = Synapse(pre=self, post=neuron)
        self.synapses[synapse.ID] = synapse
        neuron.synapses[synapse.ID] = synapse
        return synapse

    def project_from(self, neuron):
        synapse = Synapse(pre=neuron, post=self)
        neuron.synapses[synapse.ID] = synapse
        self.synapses[synapse.ID] = synapse
        return synapse

    def Synapse(self,ID:str):
        return self.synapses[ID]

    def __str__(self):
        return 'Neuron({})'.format(self.ID)
    
    def __repr__(self):
        return 'Neuron({})'.format(self.ID)
        
class Synapse:
    def __init__(self, pre, post):
        self.pre    = pre
        self.post   = post
        self.w      = round(random(), 2)
    
    def fit(self):
        relative_fr = round(self.pre.fr/(self.post.fr+1), 2)
        self.w *= relative_fr

    @property
    def ID(self):
        return '{}-{}'.format(self.pre.ID, self.post.ID)
    
    def __str__(self):
        return 'Synapse({})'.format(self.ID)
    
    def __repr__(self):
        return 'Synapse({})'.format(self.ID)

if __name__ == "__main__":
    pass