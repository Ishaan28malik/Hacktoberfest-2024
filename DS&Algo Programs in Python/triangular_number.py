"""
Python program to find the nth triangular number, 
or the sum of the first n natural numbers
"""

def triangular(n: int) -> int:
    return (n*(n+1))//2

if __name__ == "__main__":
    n = int(input("Enter the triangular number you want to find: "))
    print(triangular(n))