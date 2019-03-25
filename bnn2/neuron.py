import numpy as np
from random import random

class Neuron:
    def __init__(self,ID:str):
        self.ID         = ID
        self.synapses   = {}
        self.x          = None

    def feed(self,x):
        self.x = x

    @property
    def fr(self):
        return self._get_fr()
    
    def _get_fr(self):
        if self.x:
            return self.x
        else:
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
    n00 = Neuron('00')
    n01 = Neuron('01')
    
    n10 = Neuron('10')

    s00_10 = n00.project_to(n10)
    s01_10 = n01.project_to(n10)


    x0 = np.array(0.0)
    x1 = np.array(1.0)

    n00.feed(x1)
    n01.feed(x0)
    print('{:.2f} {:.2f} : Input Neurons\n{:.2f} {:.2f} : Synapses\n  {:.2f}    : Output Neuron'.format(
        n00.fr,n01.fr,s00_10.w,s01_10.w,n10.fr))
    s00_10.fit()
    s01_10.fit()
    print('{:.2f} {:.2f} : Input Neurons\n{:.2f} {:.2f} : Synapses\n  {:.2f}    : Output Neuron'.format(
        n00.fr,n01.fr,s00_10.w,s01_10.w,n10.fr))
    s00_10.fit()
    s01_10.fit()
    print('{:.2f} {:.2f} : Input Neurons\n{:.2f} {:.2f} : Synapses\n  {:.2f}    : Output Neuron'.format(
        n00.fr,n01.fr,s00_10.w,s01_10.w,n10.fr))
    
    n10.feed(x1)
    s00_10.fit()
    s01_10.fit()
    print('{:.2f} {:.2f} : Input Neurons\n{:.2f} {:.2f} : Synapses\n  {:.2f}    : Output Neuron'.format(
        n00.fr,n01.fr,s00_10.w,s01_10.w,n10.fr))
    # n01.feed(x0)