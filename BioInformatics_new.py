# Import math Library
import math

'''
Viterbi algorithm 
sequence = GGCT
'''

def viterbi(start_p, trans_p, emiss_p):
    
    V = {} 
    
    # compute initial probalities (start_p)
    dict = {}
    i = 1
    for s in states:  # a, b
        #p =  math.log2(emiss_p[s][sequence[0]] * start_p[s])
        p =  emiss_p[s][sequence[0]] * start_p[s]
        '''
        if p > max_p:
            max_p = p
            state = s
        '''
        dict[s] = p
        V[i] = dict
    i+=1  
          
    # deal with the rest
    for symbol in sequence[1:]:  # after the 1st symbol
        dict = {}
        for s in states:  # a, b
            max2 = -1000
            for s1 in states:
                p = emiss_p[s][symbol] * trans_p[s][s1]
                p1 = p * V[i-1][s1]
                if p1 > max2:
                    max2 = p1
            dict[s] = max2
            V[i] = dict
        i+=1
    
    print("\nDict:\n", V)
    
    # log2 dictionary items
    log_dict = {
    key: {inner_key: math.log2(value) for inner_key, value in inner_dict.items()}
    for key, inner_dict in V.items()}
    
    print("\nLog2 dict: \n", log_dict)
    
    # find the most possible sequence
    # find the max element for each key
    max_elements = {key: max(value.items(), key=lambda x: x[1]) for key, value in log_dict.items()}

    most_pos_seq = []
    print("\nMax elements for each key:")
    for key, (inner_key, value) in max_elements.items():
        print("Outside key: ",key,", Inner key: ", inner_key, ", with value: ", value)
        most_pos_seq.append(inner_key)
    
    print("\nMost possible sequence:\n",most_pos_seq)
    return 0


'''
Main programm
'''
# observation space
observations = ("A", "G", "T", "C")

sequence = ['G', 'G', 'C', 'T']

# state space
states = ("a", "b")

# dictionary of initial probabilities
start_p = {"a": 0.5, "b": 0.5} 

# transition dictionary 
trans_p = {
    "a": {"a": 0.9, "b": 0.1},
    "b": {"a": 0.1, "b": 0.9}
}

# emission dictionary
emiss_p = {
    "a": {"A": 0.4, "G": 0.4, "T": 0.1, "C": 0.1},
    "b": {"A": 0.2, "G": 0.2, "T": 0.3, "C": 0.3}
}

# call viterbi function
viterbi(start_p, trans_p, emiss_p)