#palindrome_partition

def isPalindrome(string:str, start:int, end:int): 
    while start < end: 
        if string[end] != string[start]: 
            return False
        start += 1
        end -= 1
    return True

def findAllPartitions(allPartitions, subPartitions, initial, n, string):
    if initial >= n:
        x = subPartitions.copy() 
        allPartitions.append(x)
        return

    for i in range(initial, n): 
        if isPalindrome(string, initial, i): 
 
            subPartitions.append(string[initial:i + 1]) 

            findAllPartitions(allPartitions, subPartitions, i + 1, n, string) 

            subPartitions.pop() 

def palindromePartitions(string):
    allPartitions = []
    subPartitions = []

    findAllPartitions(allPartitions, subPartitions, 0, len(string), string)
    
    for i in range(len(allPartitions)): 
        for j in range(len(allPartitions[i])): 
            print(allPartitions[i][j], end = " ") 
        print() 

string = str(input())
palindromePartitions(string) 


