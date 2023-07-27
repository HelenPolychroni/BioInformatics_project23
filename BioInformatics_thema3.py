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
    
n = len(sequence1)

''' Sequence 2'''
# open file to read
with open("sequence2.txt", "r") as file:
    # read sequence from file
    sequence2 = file.read().strip()

m = len(sequence2)

print("\nLength of 1st sequence is: (n) ",n)
print("Length of 2nd sequence is: (m) ",m)

'''
3 terminal states (n,m):
1. (1,1)
2. (x,0) for x>= 0 and x<=n 
3. (0,x) for x>= 0 and x<= m
'''

# initialize R table
def initialize_table(m, n, default_value=0):
    R = [[default_value for _ in range(n)] for _ in range(m)]
    return R

def print_table(R):
    for row in R:
        print(row)

# build the table first   m x n
def build_Rtable(m, n):
    '''
    R table with:
    m rows 
    n columns
    
    states:
    E: End of game
    W: Win
    L: Lose
    '''
    print("Function to create table here...")
    
    # let's start
    R = initialize_table(m, n)
    
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
        for i in range(1, n):
            R[r][i] = 'W'
            
    for i in range(1,n):        
        for c in range(1,3):
            R[i][c] = 'W'
            
    # initialize cell (1,1) with E value
    R[1][1] = 'E'
    
    
    # deal with the rest table
    # 3rd and 4th column after the 3rd row
    for c in range(3,n): # columns
        for r in range(3,m):  # rows
            # R[i][j]
            print(c,r)
            print("1st: ",R[c-2][r-1])
            print("2nd: ",R[c-1][r-2])
            if (R[c-2][r-1] == 'W' and R[c-1][r-2] == 'W'):
                R[c][r] = 'L'
            elif (R[c-2][r-1] == 'L' and R[c-1][r-2] == 'L'):
                R[c][r] = 'W'
            elif ((R[c-2][r-1] == 'L' or R[c-1][r-2] == 'L') and (R[c-2][r-1] == 'W' or R[c-1][r-2] == 'W')):
                R[c][r] = 'L'
            elif (R[c-2][r-1] == 'E' or R[c-1][r-2] == 'E'):
                R[c][r] = 'W'
    
    print("\nR table is:\n")
    print_table(R)
    
    return R
    

def player1_playing(n, m):  # = Human is playing
    
    flag = False
    print("\nPlayer1 is playing:")
    
    #if ((n != 0 or m != 0) and (n !=1 and m != 1)):
    if ((n >= 1 and m >= 2) or (n >= 2 and m >= 1 )):
        
        sequence = None
       
        while (sequence != "1" and sequence != "2"):
            
            sequence = input("Choose from which sequence you want to remove 2 nucleotides (type 1 or 2): ")
           
            if (sequence != "1" and sequence != "2"):
                print("Invalid input. Please type 1 or 2.")
            elif ((sequence == '1' and n < 2 ) or (sequence == '2' and m < 2)):
                sequence = input("Not enough number of noucleotides to be removed, choose again: ")    
           
        #print("2 noucleotides have just been removed from sequence no",sequence,".")
        #print("1 noucleotide has just been removed from the other sequence.")
        
        if (sequence == '1'):
            n = n - 2
            m = m -1
            
        else:  # sequence == '2'
            m = m - 2
            n = n - 1
         
        print("\nnew n: ", n)
        print("new m:", m)
            
        #if ((n == 0 and m == 0) or (n == 1 and m == 1 ) or (n == 0 or m == 0)):
            #print("Player2 wins!")
            #flag = True
    
        
        #if (flag == False):
            
        player2_playing(n, m)
        '''
        else:
            print("Out of moves")
            print("Player2 wins!")
            print("Game ends!")
        '''
    else:
        print("\nOut of moves.")
        print("Player1 wins!")
        print("\nGame ends!")
    

def player2_playing(n, m):  # Computer is playing
    
    print("\nPlayer2 is playing (computer):")    
    
    flag = False
    
    #if ((n != 0 or m != 0) and (n !=1 and m != 1)):
    if ((n >= 1 and m >= 2) or (n >= 2 and m >= 1 )):
        
        # find the sequence with the max length and remove 2 noucleotides from this
        max1 = max(n,m)
        
        if (max1 == n):  # 1st sequence
            n -= 2
            m -= 1
        else:            # 2nd sequence
            m -= 2
            n -= 1
            
        '''    
        r = random.randint(1, 2)  # randomly choose the number of noucleotides to be removed from 1st sequence
        sequence_list = [m, n]
        random_sequence = random.choice(sequence_list)
        
        if(random_sequence == n and n >= r):  # 1st sequence
            n = n - r
            
            r1 = 2
            
            if (r != r1):
                if (m >= r1):
                    m = m - r1
            else:
                m = m - 1
        '''
        
        print("Player2 has just played.")
        
        print("\nnew n: ", n)
        print("new m:", m)
        
        '''
        if ((n == 0 and m == 0) or (n == 1 and m == 1 ) or (n == 0 or m == 0)):
            #print("Player1 wins!")
            flag = True
    
        if (flag == False):
        '''
        player1_playing(n, m)
        
        '''
        else:
            print("Player1 wins!")
            print("Game ends!")
        '''
    else:
        print("\nOut of moves.")
        print("Player2 wins!")
        print("\nGame ends!")
        

def game_strategy(R, m, n, num):
    
    next = 0   # next player
    if (num == 1):
        next = 2
    else:
        next = 1
        
    print("\nPlayer", num," is playing.")
    
    flag = False   
    #while (flag == False):
        
    if (R[m-2][n-1] == 'W' and R[m-1][n-2] == 'W'):  # both W states
        move = random.choice([1, 2])
        if (move == 1):
            m = m -2
            n = n-1
        else:
            m = m - 1
            n = n -2
    
    elif (R[m-2][n-1] == 'W' and R[m-1][n-2] == 'L'):  
        # choose W state
        m = m - 2
        n = n - 1
        
    elif (R[m-2][n-1] == 'L' and R[m-1][n-2] == 'W'):
        # choose W state
        m = m - 1
        n = n - 2
        
    elif (R[m-2][n-1] == 'L' and R[m-1][n-2] == 'L'):
        move = random.choice([1, 2])
        if (move == 1):
            m = m - 2
            n = n - 1 
        else:
            m = m - 1
            n = n - 2
        
    elif (R[m-2][n-1] == 'E') :
        m = m - 2
        n = n - 1 
            
    elif (R[m-1][n-2] == 'E') :
        m = m - 1
        n = n - 2
        
    if (R[m][n] == 'E'):
        # we have a winner
        print("\nOut of moves")
        print("Winner: player", num)   
        flag = True
        
   
    if (flag == False) : 
        
        print("\nnew n: ", n)
        print("new m: ",m)     
       
        game_strategy(R, m, n, next)
    
    #print("\nWinner: ",player)   
    return 0    
        

# main programm
n = 5   # columns
m = 5   # rows

# call function to build the R table
R = build_Rtable(m, n)


print("\nn: ", n)
print("m: ", m)
print("---------------")
print("\nGame is starting:")
#players_list = ["Player 1", "Player2"]

# Choose randomly a player to start the game
random_player = random.randrange(1,3)
#if (random_player == players_list[0]):
    #player1_playing(n, m)
game_strategy(R, m, n, random_player)
#else:
#game_strategy(R, m, n, random_player)
    #player2_playing(n, m)
    

   