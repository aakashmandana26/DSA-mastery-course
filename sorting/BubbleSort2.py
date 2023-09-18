numbers = [6,3,7,2,8,4,5,1]

def Bubble2(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
    
print(numbers)
Bubble2(numbers)
print(numbers)
