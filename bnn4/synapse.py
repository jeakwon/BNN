class Synapse:
    def __init__(self, synapse_layer, pre_ID, post_ID, nn):
        self.synapse_layer = synapse_layer
        self.pre_ID = pre_ID
        self.post_ID = post_ID
        self.nn = nn
        self.w = 0
        
    def __repr__(self):
        return 's({},{},{})'.format(self.synapse_layer, self.pre_ID, self.post_ID)