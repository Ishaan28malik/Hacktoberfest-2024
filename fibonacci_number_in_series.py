def fib(n): 
    phi = ((1 + (5 ** (1 / 2))) / 2); 
    return round((phi ** n) / (5 ** (1 / 2))); 
  
# Function to return the required sum 
def calculateSum(l, r): 
      
    # To store the sum 
    sum = 0; 
  
    # Calculate the sum 
    for i in range(l, r + 1): 
        sum += fib(i); 
  
    return sum; 

# Taking inputs from user
z,x = map(int,input().split())
# Driver Code 
if __name__ == '__main__': 
    l, r = 4, 8; 
    print(calculateSum(z, x)); 
