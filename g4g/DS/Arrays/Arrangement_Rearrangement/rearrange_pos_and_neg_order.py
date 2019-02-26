'''
   ** Asked
   Rearrange array in alternating positive & negative items with O(1) extra space
   ** Maintaining order
'''
# ********** NOT IMPLEMENTED BY ME ********
# *********** COPIED SOLUTION *************

def rightRotate(arr, n, outOfPlace, cur): 
	temp = arr[cur] 
	for i in range(cur, outOfPlace, -1): 
		arr[i] = arr[i - 1] 
	arr[outOfPlace] = temp 
	return arr

def rearrange(arr): 
    n = len(arr)
    outOfPlace = -1
    for index in range(n): 
        if(outOfPlace >= 0): 
  
            # if element at outOfPlace place in  
            # negative and if element at index 
            # is positive we can rotate the  
            # array to right or if element 
            # at outOfPlace place in positive and 
            # if element at index is negative we  
            # can rotate the array to right 
            if((arr[index] >= 0 and arr[outOfPlace] < 0) or 
               (arr[index] < 0 and arr[outOfPlace] >= 0)): 
                arr = rightRotate(arr, n, outOfPlace, index) 
                if(index-outOfPlace > 2): 
                    outOfPlace += 2
                else: 
                    outOfPlace =- 1
                      
        if(outOfPlace == -1): 
            print index
            # conditions for A[index] to  
            # be in out of place 
            if((arr[index] >= 0 and index % 2 == 0) or 
               (arr[index] < 0 and index % 2 == 1)): 
                outOfPlace = index
                print 'OFI', outOfPlace, 'index', index
        print arr
    return arr

rearrange([1, 2, 3, -4, -1, 4])