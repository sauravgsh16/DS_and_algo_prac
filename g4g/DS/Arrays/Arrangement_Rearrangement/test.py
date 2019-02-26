import array as a 

def rearrangeArr(arr, n):  
    # total even positions 
    evenPos = int(n / 2) 
  
    # total odd positions 
    oddPos = n - evenPos 
  
    # intialising empty array in python 
    tempArr = [None] * len(arr) 
  
    # copy original array in an 
    # auxiliary array 
    for i in range(0, n): 
          
        tempArr[i] = arr[i] 
  
    # sort the auxiliary array 
    tempArr.sort() 
  
    j = oddPos - 1
  
    # fill up odd position in original 
    # array 
    print arr
    for i in range(0, n, 2): 
  
        arr[i] = tempArr[j] 
        j = j - 1
    print arr
      
    j = oddPos 
  
    # fill up even positions in original 
    # array 
    for i in range(1, n, 2): 
        arr[i] = tempArr[j] 
        j = j + 1
      
    # display array 
    print arr

arr = [ 1, 2, 1, 4, 5, 6, 8, 8, 9, 9]
rearrangeArr(arr, len(arr))