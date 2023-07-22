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