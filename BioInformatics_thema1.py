# Import math Library
import math

'''
Viterbi algorithm 
sequence = GGCT
'''
def viterbi(observations, states, initial_p, trans_p, emiss_p):
    
    V = [{}] # list dict to handle keys and values for each stage
    
    # compute initial probalities (initial_p)
    i = 0
    for s in states:  # a, b
        p =  emiss_p[s][observations[0]] * initial_p[s]
        V[i][s] = {"prob": p, "prev_node": None}
    
    i+=1        
    # deal with the rest
    for symbol in observations[1:]:  # after the 1st symbol
        V.append({})
        for s in states:  # a, b
            p1 = trans_p[states[0]][s] * V[i-1][states[0]]["prob"]
            prev_s = states[0]
            for s1 in states[1:]:
                p2 = trans_p[s1][s] * V[i-1][s1]["prob"]
                if p1 > p2:
                    max2 = p1
                else: 
                    max2 = p2 
                    prev_s = s1
                
            max_p = max2  * emiss_p[s][symbol]  # get the max probability
            V[i][s] = {"prob": max_p, "prev_node": prev_s}
        i+=1
    
    
    # log2 list items because of overflow
    for dictionary in V:
        for key, value in dictionary.items():
            if 'prob' in value:
                value['prob'] = math.log(value['prob'])
    
    print("\nLog2 items: \n", V)
    
    
    '''
    find the most possible sequence 
    1. find the maximum probability state for the last element
    2. backtracking following the previous states/nodes
    '''
    pos_sequence = [] # most possible sequence
    max_p = -1000.0   # max probability
    best_state = None
    
    # find the maximum probability state for the last element of the sequence
    for state, data in V[-1].items():
        if data["prob"] > max_p:
            max_p = data["prob"]
            best_state = state
    pos_sequence.append(best_state)
    previous = best_state   # previous state
    
    # backtracking
    for i in range(len(V) - 1, 0, -1):
        pos_sequence.insert(0, V[i][previous]["prev_node"])
        previous = V[i][previous]["prev_node"]
 
    print ("\nMost possible sequence is: ", pos_sequence ," with highest probability of ", max_p)
 

'''
Main programm
'''

# observation space
observations = ("G", "G", "C", "T")

# state space
states = ("a", "b")

# dictionary of initial probabilities
initial_p = {"a": 0.5, "b": 0.5} 

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

# print some usefull stuff
print("\nObservation sequence is: ", observations)
print("\nHidden states are: ", states)
print("Initial probabilities are: ", initial_p)
print("Transition dictionary is: ", trans_p)
print("Emission dictionary is: ", emiss_p)
print("-----------------------------------------------------------------------------------------------------------------------")

# call viterbi function
viterbi(observations, states, initial_p, trans_p, emiss_p)
