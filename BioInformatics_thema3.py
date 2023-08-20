import random

'''
Problem 6.14 
2 sequences (n and m length)
'''

''' Sequence 1'''
# open file to read
with open("sequence1.txt", "r") as file:
    # read sequence from file
    sequence1 = file.read().strip()
    
m = len(sequence1)

''' Sequence 2'''
# open file to read
with open("sequence2.txt", "r") as file:
    # read sequence from file
    sequence2 = file.read().strip()

n = len(sequence2)

print("\nLength of 1st sequence is: (m) ",m)
print("Length of 2nd sequence is: (n) ",n)


# initialize R table
def initialize_table(m, n, default_value=0):
    R = [[default_value for _ in range(n)] for _ in range(m)]
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
    
    # initialize 1st row with E value
    i = 0
    for j in range(n):
        R[i][j] = 'E'
    
    # initialize 1st column with E value
    for j in range(m):
        R[j][i] = 'E'
    
    # initialize cell (1,1) with E value
    R[1][1] = 'E'
    
    # initialize 2nd and 3rd row, column with W value
    for r in range(1,3):  
        for i in range(1, n):  # number of columns
            R[r][i] = 'W'
            
    for i in range(1,m):      # number of rows
        for c in range(1,3):
            R[i][c] = 'W'
            
    # initialize cell (1,1) with E value
    R[1][1] = 'E'
    
    
    # deal with the rest table
    # 3rd till m column after the 3rd row
    for c in range(3,m): # columns
        for r in range(3,n):  # rows
            # R[i][j]
            if (R[c-2][r-1] == 'W' and R[c-1][r-2] == 'W'):
                R[c][r] = 'L'
            elif (R[c-2][r-1] == 'L' or R[c-1][r-2] == 'L'):
                R[c][r] = 'W'
            '''    
            elif (R[c-2][r-1] == 'L' and R[c-1][r-2] == 'L'):
                R[c][r] = 'W'
            elif ((R[c-2][r-1] == 'L' or R[c-1][r-2] == 'L') and (R[c-2][r-1] == 'W' or R[c-1][r-2] == 'W')):
                R[c][r] = 'W' #  or L
            '''
            #elif (R[c-2][r-1] == 'E' or R[c-1][r-2] == 'E'):
            #    R[c][r] = 'W'
    
    print("\nR table is:\n")
    print_table(R)
    
    return R
    

def game_strategy(R, m, n, num):
    
    
    next = 0   # next player
    if (num == 1):
        next = 2
    else:
        next = 1
        
    print("\nPlayer", num," is playing:")
    
    flag = False   
    
    if (R[m][n] == 'E'):
        # we have a winner
        print("Out of moves")
        print("\nWinner: Player", num)   
        flag = True
    
    
    if (R[m-2][n-1] == 'W' and R[m-1][n-2] == 'W'):  # both W states
        move = random.choice([1, 2])
        if (move == 1):
            m = m - 2
            n = n - 1
        else:
            m = m - 1
            n = n - 2
    
    elif (R[m-2][n-1] == 'W' and R[m-1][n-2] == 'L'):  
        # choose L state
        m = m - 1
        n = n - 2
        
    elif (R[m-2][n-1] == 'L' and R[m-1][n-2] == 'W'):
        # choose L state
        m = m - 2
        n = n - 1
        
    elif (R[m-2][n-1] == 'L' and R[m-1][n-2] == 'L'):
        # choose random a L state
        move = random.choice([1, 2])
        if (move == 1):
            m = m - 2
            n = n - 1 
        else:
            m = m - 1
            n = n - 2
    
        
    elif ((R[m-2][n-1] == 'E') and (R[m-1][n-2] == 'E')) :
        move = random.choice([1, 2])
        if (move == 1):
            m = m - 2
            n = n - 1 
        else:
            m = m - 1
            n = n - 2   
    
    
    elif (R[m-2][n-1] == 'E') : # game is about to end
        m = m - 2
        n = n - 1 
            
    elif (R[m-1][n-2] == 'E') : # game is about to end
        m = m - 1
        n = n - 2
    
    
    if (flag == False) : 
        
        print("New m: ",m)
        print("New n: ", n)
           
        game_strategy(R, m, n, next)
    
    
# main programm
m = 4   # rows
n = 5   # columns

print("\nLength of 1st sequence is: (m) ",m)
print("Length of 2nd sequence is: (n) ",n)

# call function to build the R table
R = build_Rtable(m+1, n+1)

print("\nLast table cell's position: (",m,",",n,")")
print("\nLast table cell's value: ",R[m][n])
print("-------------------------------------")
print("\nGame is starting:")

# Choose randomly a player to start the game
random_player = random.randrange(1,3)
game_strategy(R, m, n, random_player)


   