def fibonacciRecursive(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

print(fibonacciRecursive(6))