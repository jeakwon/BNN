import random

def overlap(a, b):
    return not set(a).isdisjoint(b)

class Network:
    next_neuron_ID  = 0
    next_synapse_ID = 0
    neurons     = {}
    synapses    = {}
    
    def __init__(self, ID=0):
        self.ID = ID
        print(f'"{self}" created')

    def neurogenesis(self, n_times=1):
        for _ in range(n_times):
            new_neuron = Neuron(network=self, ID=self.next_neuron_ID)
            self.neurons[self.next_neuron_ID]=new_neuron
            self.next_neuron_ID+=1
            print(f'{new_neuron} created')
        return self

    def synaptogenesis(self, random_genesis=True, n_times=1, pre=None, post=None):
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
    dendrite    = []
    axon        = []
    dendrite_syn_IDs = []
    axon_syn_IDs     = []

    def __init__(self, network, ID, threshold=0):
        self.network = network
        self.ID = ID
        self.threshold = threshold

    def project_to(self, other):
        # protect recursion
        print(other.dendrite_syn_IDs, self.axon_syn_IDs)
        if overlap(other.dendrite_syn_IDs, self.axon_syn_IDs):
            print(f'reverse synapse already exist')
            return self
        new_synapse = Synapse(ID=self.network.next_synapse_ID, pre=self, post=other)
        self.network.synapses[self.network.next_synapse_ID]=new_synapse
        self.axon.append(new_synapse)
        self.axon_syn_IDs.append(new_synapse.ID)
        other.dendrite.append(new_synapse)
        other.dendrite_syn_IDs.append(new_synapse.ID)
        self.network.next_synapse_ID+=1
        print(f'{new_synapse} created')
        return self

    def project_from(self, other):
        # protect recursion
        if overlap(other.axon_syn_IDs, self.dendrite_syn_IDs):
            print(f'reverse synapse already exist')
            return self
        new_synapse = Synapse(ID=self.network.next_synapse_ID, pre=other, post=self)
        self.network.synapses[self.network.next_synapse_ID]=new_synapse
        other.axon.append(new_synapse)
        other.axon_syn_IDs.append(new_synapse.ID)
        self.dendrite.append(new_synapse)
        self.dendrite_syn_IDs.append(new_synapse.ID)
        self.network.next_synapse_ID+=1
        print(f'{new_synapse} created')
        return self

    def __repr__(self):
        return f'Neuron({self.ID})'
    
    def __str__(self):
        return f'Neuron({self.ID})'

class Synapse:
    def __init__(self, ID, pre=None, post=None, weight=0.5):
        self.ID     = ID
        self.pre    = pre
        self.post   = post
        self.weight = weight

    def __repr__(self):
        return f'Synapse({self.ID})'

    def __str__(self):
        return f'Synapse({self.ID})'

if __name__ == "__main__":
    network = Network()
    network.neurogenesis(10)
    network.synaptogenesis(n_times=10)
    # a = [1,2,3,]
    # b = [3,4,5,]
    # print(set(a).isdisjoint(b))
