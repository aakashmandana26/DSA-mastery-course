numbers = [6,3,7,2,8,4,5,1]

def Bubble(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i],arr[j]=arr[j],arr[i]

    return arr

print(Bubble(numbers))