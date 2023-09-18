array1 = ['a', 'b', 'c', 'a']
array2 = ['z', 'y', 'r']
map={}
def containsCommonItem(arr1, arr2):
    for item in arr1:
        map[item]=True
    print(map)
    
    for item in arr2: 
        
        if(map.get(item)!=None):
            return True
    return False

print(containsCommonItem(array1, array2))


  