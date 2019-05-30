'''
   Minimum sum of squares of character counts in a given string after removing
   k characters
'''

'''
   Eg:
   str = abcccc, k = 1
   char freq = a - 1, b - 1, c - 3
   Thus we remove 'k' c, since it has the max freq and get:
   sum = 1^2 + 1^2 + 2^2
'''
'''
   A simple solution is to use sorting technique through all current highest
   frequency reduce up to k times. After every reduce again sort frequency array

   A Better solution is to use a Priority Queue, which has highest element at the
   top
'''
from Queue import PriorityQueue

MAX_CHAR = 26

def min_string_value(string, k):
    l = len(string)

    if k >= l:
        return 0
    
    freq = [0] * MAX_CHAR

    for i in range(l):
        freq[ord(string[i]) - 97] += 1

    queue = PriorityQueue()
    for i in freq:
        if i > 0:
            queue.put(-i)
    
    while k > 0:
        # we pop the max element, decrease the freq by 1 (in the case, we add 1,
        # since we have the queue updated with -ve values)
        temp = queue.get()
        temp = temp + 1
        queue.put(temp)
        k -= 1

    result = 0
    # Get all elements from queue, multiply by -1 to make them positive
    # and add them to result
    while not queue.empty():
        temp = queue.get()
        temp = temp * (-1)
        result += temp * temp
    
    return result

print min_string_value('abbccc', 2)
