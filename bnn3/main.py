from neuralnet import NN

if __name__ == "__main__":
    nn = NN(3,2,1)
    print(nn.synapses)
    pre_count = 3
    post_count = 2
    mat = [[0 for x in range(post_count)] for x in range(pre_count)] 
    print(mat[0][2])