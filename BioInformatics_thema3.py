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
    
    print("\nPlayer2 is playing:")    
    
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
        
        
        

# main programm
n = 6
m = 1
print("\nn: ", n)
print("m: ", m)
print("---------------")
print("\nGame is starting:")
players_list = ["Player 1", "Player2"]

# Choose randomly a player to start the game
random_player = random.choice(players_list)
if (random_player == players_list[0]):
    player1_playing(n, m)
else:
    player2_playing(n, m)
    

   