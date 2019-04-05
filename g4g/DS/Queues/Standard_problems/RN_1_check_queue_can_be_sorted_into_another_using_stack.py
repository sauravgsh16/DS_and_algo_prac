''' Check if a queue can be sorted into another queue using stack '''

'''
   Algorithm:
   1. Initialize the expected_element = 1
   2. Check if either front element of given Queue or top element of the stack 
      have expected_element
      a) If yes, increment expected_element by 1, repeat step 2.
      b) Else, pop front of Queue and push it to the stack. 
         If the popped element is greater than top of the Stack, return 'No'.
'''

from Queue import Queue

def check_sorted(q):
    n = q.qsize()
    stack = []
    expected = 1
    front = None

    while not q.empty():
        front = q.get()
        if front == expected:
            expected += 1
        else:
            if len(stack) != 0 and stack[-1] < front:
                return False
            else:
                stack.append(front)
        while len(stack) != 0 and stack[-1] == expected:
            stack.pop()
            expected += 1
    
    if expected - 1 == n and len(stack) == 0:
        return True
    return False

q = Queue()
q.put(5)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
print check_sorted(q)