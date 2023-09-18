numbers = [6,3,7,2,8,4,5,1]
print(numbers)
def InsertionSorting(arr):
    
    reset=1
    while reset<=len(arr)-1:
        i=reset
        while i>=1 and i<=len(arr)-1 and arr[i]<arr[i-1]:
            
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i-=1
            
    
        reset+=1
        

InsertionSorting(numbers)
print(numbers)

        


