import numpy as np
class Neuron:
    def __init__(self,fr=0,upper_neurons=None):
        self.fr=fr

class Synapse:
    def __init__(self, w, pre=None, post=None):
        self.w = w
        self.pre = pre
        self.post = post

    def fit(self, dw=0):
        fitter = lambda x: max(0.001,x) if x<1 else 1
        self.w = fitter(self.w * self.dw)
        if self.w is 1:
            self.pre.fr = fitter(self.pre.fr * self.dw)

    @property
    def output(self):
        return self.pre.fr*self.w
    
    @property
    def delta(self):
        return self.post.fr-self.output

    @property
    def dw(self):
        return 2**self.delta


if __name__ == "__main__":
    import random
    w = random.uniform(0,1)
    pre = Neuron(0.01)
    pre2 = Neuron(0.99)
    post = Neuron(0.5)
    syn = Synapse(w,pre,post)
    syn2 = Synapse(w,pre2,post)
    print('{:>10},{:>10},{:>10},{:>10},{:>10}'.format('pre.fr','weight','delta','output','post.fr'))
    print('{:10.3f},{:10.3f},{:10.3f},{:10.3f},{:10.3f}'.format(syn.pre.fr, syn.w, syn.delta, syn.output, syn.post.fr))
    print('{:10.3f},{:10.3f},{:10.3f},{:10.3f},{:10.3f}'.format(syn2.pre.fr, syn2.w, syn2.delta, syn2.output, syn2.post.fr))
    for i in range(20):
        syn.fit()
        syn2.fit()
        print('{:10.3f},{:10.3f},{:10.3f},{:10.3f},{:10.3f}'.format(syn.pre.fr, syn.w, syn.delta, syn.output, syn.post.fr))
        print('{:10.3f},{:10.3f},{:10.3f},{:10.3f},{:10.3f}'.format(syn2.pre.fr, syn2.w, syn2.delta, syn2.output, syn2.post.fr))