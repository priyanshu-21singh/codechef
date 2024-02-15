def FindRepeatingElement(arr, size): 
    for i in range(size): 
        for j in range(i+1, size): 
            if arr[i] == arr[j]: 
                return arr[i] 
    return -1
  
# Driver code 
if __name__ == '__main__': 
    arr = [1, 2, 3, 4,5,6,6,7] 
    n = len(arr) 
    element = FindRepeatingElement(arr, n) 
    if element != -1: 
        print(element)