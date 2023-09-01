import random

'''
Problem 
2 sequences (n and m length)
'''

''' Sequence 2'''
with open("sequence2.txt", "r") as file:
    sequence2 = file.read().strip()

m = len(sequence2)

''' Sequence 3'''
with open("sequence3.txt", "r") as file:
    sequence3 = file.read().strip()
    
n = len(sequence3)

print("Length of 2nd sequence is: (m) ",m)
print("Length of 1st sequence is: (n) ",n)


# initialize R table
def initialize_table(m, n, default_value=0):
    R = [[default_value for _ in range(n+1)] for _ in range(m+1)]
    return R

# print R table
def print_table(R):
    for row in R:
        print(row)

# fill the R table with values
def build_Rtable(m, n):
    '''
    R table with:
    m rows 
    n columns
    
    states (values):
    E: End of game
    W: Win
    L: Lose
    '''
    
    # let's start
    R = initialize_table(m, n)
    
    # Number of rows
    num_rows = len(R)

    # Number of columns (assuming all rows have the same length)
    num_columns = len(R[0])

    # Printing the results
    print("\nNumber of rows:", num_rows)
    print("Number of columns:", num_columns)

    #initialize (0,0) with E value
    R[0][0] = 'E'

    # initialize 1st row with W value
    for j in range(1,n+1):
        R[0][j] = 'W'
    
    # initialize 1st column with W value
    for j in range(1,m+1):
        R[j][0] = 'W'
    
    # initialize cell (i,i) with W value
    for i in range (1,n+1):
        R[i][i] = 'W'
    
    #rest table with 'L'
    for i in range(m+1):
        for j in range(n+1):
            if R[i][j] != 'E' and R[i][j] != 'W':
               R[i][j] = 'L'

    print("\nR table is:\n")
    print_table(R)
    return R


def game_strategy(R, m, n, num):
    
    if (m==0):
        rndm = random.randint(1,n)
    elif (n==0):
        rndm = random.randint(1,m)
    else:
        rndm = random.randint(1,min(m,n))
        
    

    next = 0   # next player
    if (num == 1):
        next = 2
    else:
        next = 1
       
        
    print("\nPlayer", num," is playing:")
    print('Random number: ', rndm)
    print('Current position: R[',m,'][', n,']')
    
    flag = False   # false means noone wins, you have rounds to play yet
    
    if (R[m][n] == 'E'):
        print("Out of moves. \nLoser: Player", num)
        flag = True
    elif (R[m][0] == 'W' and rndm == m and n == 0) or \
        (R[0][n] == 'W' and rndm == n and m == 0) or \
        (R[m][n] == 'W' and m == n and rndm == n):
        m = 0
        n = 0
        flag = True

    if(R[m][n]=='E'):
        flag = True
        print("You removed all nucleotides successfully. \nWinner: Player",num)



    #if any move you do is winning for the rival, do one of them randomly, its the same
    if (R[m-rndm][n-rndm] == 'W' and R[m-rndm][n] == 'W' and R[m][n-rndm] == 'W'):  # WWW states
        
        move = random.choice([1,3])
        
        if (move == 1) and (m-rndm>=0) and (n-rndm>=0):
            m = m - rndm
            n = n - rndm
        elif (move == 2) and (m-rndm>=0):
            m = m - rndm
        elif (n-rndm>=0):
            n = n - rndm

    elif (R[m-rndm][n-rndm] == 'L' and R[m-rndm][n] == 'W' and R[m][n-rndm] == 'W') and (m-rndm>=0) and (n-rndm>=0):  # LWW states
        # choose L state
        m = m - rndm
        n = n - rndm

    elif (R[m-rndm][n-rndm] == 'W' and R[m-rndm][n] == 'L' and R[m][n-rndm] == 'W' and (m-rndm>=0)):  # WLW states
        # choose L state
        m = m - rndm
        
    elif (R[m-rndm][n-rndm] == 'W' and R[m-rndm][n] == 'W' and R[m][n-rndm] == 'L' and (n-rndm>=0)):  # WWL states
        # choose L state
        n = n - rndm

    elif (R[m-rndm][n-rndm] == 'L' and R[m-rndm][n] == 'L' and R[m][n-rndm] == 'L'):  # LLL states
        move = random.choice([1,3])
        if (move == 1) and (m-rndm>=0) and (n-rndm>=0) :
            m = m - rndm
            n = n - rndm
        elif (move == 2) and (m-rndm>=0) :
            m = m - rndm
        elif (n-rndm>=0)  :
                n = n - rndm

    elif (R[m-rndm][n-rndm] == 'W' and R[m-rndm][n] == 'L' and R[m][n-rndm] == 'L'): #WLL states
        # choose L state
        move = random.choice([1,2])
        if (move == 1) and (m-rndm>=0):
            m = m - rndm
        elif (n-rndm>=0):
            n = n - rndm
       
    elif (R[m-rndm][n-rndm] == 'L' and R[m-rndm][n] == 'W' and R[m][n-rndm] == 'L'): #LWL states
        # choose L state
        move = random.choice([1,2])
        if (move == 1) and (m-rndm>=0) and (n-rndm>=0):
            m = m - rndm
            n = n - rndm
        elif (n-rndm>=0) :
            n = n - rndm

    elif (R[m-rndm][n-rndm] == 'L' and R[m-rndm][n] == 'L' and R[m][n-rndm] == 'W'): #LLW states
        # choose L state
        move = random.choice([1,2])
        if (move == 1) and (m-rndm>=0) and (n-rndm>=0):
            m = m - rndm
            n = n - rndm
        elif (m-rndm>=0) :
            m = m - rndm
    
    if (flag == False) : 
        print("New m: ",m)
        print("New n: ", n)
            
        game_strategy(R, m, n, next)


# main programm

m = 4   # rows
n = 3   # columns

# call function to build the R table
R = build_Rtable(m, n)

print("\nGame is starting:")

# Choose randomly a player to start the game
random_player = random.randrange(1,2)
game_strategy(R, m, n, random_player)