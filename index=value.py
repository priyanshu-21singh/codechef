def binarySearch(arr, low, high): 
    if high >= low : 
          
        mid = low + (high - low)//2
        if mid == arr[mid]:  
            return mid 
        res = -1
        if mid + 1 <= arr[high]: 
            res = binarySearch(arr, (mid + 1), high) 
        if res !=-1: 
            return res 
        if mid-1 >= arr[low]: 
            return binarySearch(arr, low, (mid -1)) 
      
  
    #  no Fixed Point  then return  -1.
    return -1
  
  
  
  

arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100] 
n = len(arr) 
print("Fixed Point is " + str(binarySearch(arr, 0, n-1))) 