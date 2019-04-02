class Synapse:
    def __init__(self,pre,post):
        self.pre    = pre
        self.post   = post

    @property
    def ID(self):
        return "L{}N{}-L{}N{}".format(self.pre.layer.ID,self.pre.ID,self.post.layer.ID,self.post.ID)

    def __repr__(self):
        return "Synapse({})".format(self.ID)

    def __str__(self):
        return "Synapse({})".format(self.ID)
