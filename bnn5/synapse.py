import time
import random
import numpy as np

def overlap(a, b):
    return not set(a).isdisjoint(b)
    
def runtime(func):
    # @wraps(func)
    def decorated(*args, **kwargs):
        before  = time.time() # Decorate front of func
        output  = func(*args, **kwargs)
        after   = time.time() # Decorate back of func
        print('Elapsed time: {}'.format(after-before))
        return output
    return decorated

class Network:
    next_neuron_ID  = 0
    neurons     = {}
    synapses    = {}

    def __init__(self, ID=0):
        self.ID = ID
        print(f'"{self}" created')
    
    def Neuron(self, ID):
        return self.neurons.get(ID)

    def Synapse(self, pre, post):
        return self.synapses.get((pre, post))

    def set_in_out_neurons(self, in_ID, out_ID):
        self.input_neuron = self.Neuron(in_ID)
        self.output_neuron = self.Neuron(out_ID)

    def navigate(self):
        level1 = self.Synapse(self.input_neuron.ID, self.output_neuron.ID)
        print(f'level1:{level1}')

        # print(
        set(
            [syn.post for syn in self.input_neuron.axon.copy()]
        ) & set(
            [syn.pre for syn in self.output_neuron.dendrite.copy()]
            ))


        
    @runtime
    def neurogenesis(self, n_times=2):
        for _ in range(n_times):
            new_neuron = Neuron(network=self, ID=self.next_neuron_ID)
            self.neurons[self.next_neuron_ID]=new_neuron
            self.next_neuron_ID+=1
            print(f'{new_neuron} created')
        return self
    
    @property
    def total_synapses(self):
        return len(self.synapses)

    @property
    def total_neurons(self):
        return len(self.neurons)

    @runtime
    def synaptogenesis(self, n_times=1, random_genesis=True, pre=None, post=None):
        if random_genesis:
            for _ in range(n_times):
                neurons = [neuron for neuron in self.neurons.values()]
                pre = random.choice(neurons)
                neurons.remove(pre)
                post = random.choice(neurons)
                pre.project_to(post)
        pre.project_to(post)
        return self



    def __repr__(self):
        return f'Network({self.ID})'
    
    def __str__(self):
        return f'Network({self.ID})'

class Neuron:
    def __init__(self, network, ID, threshold=0):
        self.network            = network
        self.ID                 = ID
        self.threshold          = threshold
        self.dendrite           = []
        self.axon               = []

    def project_to(self, other):
        # protect recursion
        if overlap(other.dendrite, self.axon):
            print(f'reverse synapse already exist')
            return self

        new_synapse = Synapse(pre=self, post=other)
        self.network.synapses[new_synapse.ID]=new_synapse

        self.axon.append(new_synapse)
        other.dendrite.append(new_synapse)
        print(f'{new_synapse} created')
        return self

    def project_from(self, other):
        # protect recursion
        if overlap(other.axon, self.dendrite):
            print(f'reverse synapse already exist')
            return self

        new_synapse = Synapse(pre=other, post=self)
        self.network.synapses[new_synapse.ID]=new_synapse

        other.axon.append(new_synapse)
        self.dendrite.append(new_synapse)
        print(f'{new_synapse} created')
        return self

    def __repr__(self):
        return f'Neuron({self.ID})'
    
    def __str__(self):
        return f'Neuron({self.ID})'

class Synapse:
    def __init__(self, pre=None, post=None, weight=0.5):
        self.pre    = pre
        self.post   = post
        self.ID     = (pre.ID, post.ID)
        self.weight = weight

    def __repr__(self):
        return f'Synapse{self.ID}'

    def __str__(self):
        return f'Synapse{self.ID}'

if __name__ == "__main__":
    net = Network()
    net.neurogenesis(n_times=1000)
    net.synaptogenesis(n_times=100000)
    net.set_in_out_neurons(1,2)
    net.navigate()
