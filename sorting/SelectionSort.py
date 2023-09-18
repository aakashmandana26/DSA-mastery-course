from cmath import inf


numbers = [6,3,7,2,8,4,5,1]

def selectionSort(arr):
    
    
    i=0
    while i<len(arr):
        minNum = float(inf)
        
        for j in range(i,len(arr)):
            if arr[j] < minNum:
                minNum = arr[j]
                pos = j
        arr[i],arr[pos]=minNum,arr[i]
        i+=1



print(numbers)
selectionSort(numbers)
print(numbers)



    