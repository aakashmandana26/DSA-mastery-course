arr=[]



def fib(n):
    
    
    
    if(n==0):
        return 0
    elif(n==1):
        return 1
    a,b=0,1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return c
    
    
    
        
    
    

print(fib(5))