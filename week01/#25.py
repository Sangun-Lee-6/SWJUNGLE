def Factorial(n):
    
    if n==0:
        return 1
    
    else :
        return n * Factorial(n-1)
    

import sys

n = int(sys.stdin.readline())

print(Factorial(n))
