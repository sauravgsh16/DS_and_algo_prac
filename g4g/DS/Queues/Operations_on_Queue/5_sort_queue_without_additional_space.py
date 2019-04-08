''' Sort a Queue without any additional space '''

import sys
from Queue import Queue

def get_min_index(q, sortedIndex):
    '''
       Queue elements after sortedIndex are already sorted.
       Finds the index of the element which is minimum
    '''
    minIndex = -1
    minVal = sys.maxsize
    n = q.qsize()
    for i in range(n):
        cur = q.get()

        if cur <= minVal and i <= sortedIndex:
            minIndex = i
            minVal = cur
        q.put(cur)
    return minIndex


def insert_min_to_rear(q, minIndex):
    n = q.qsize()
    min_val = None
    for i in range(n):
        cur = q.get()
        if i != minIndex:
            q.put(cur)
        else:
            min_val = cur
    q.put(min_val)


def sort_queue(q):
    for i in range(1, q.qsize()+1):
        minIndex = get_min_index(q, q.qsize() - i)
        insert_min_to_rear(q, minIndex)

q = Queue()
for i in [30, 11, 15, 4]:
    q.put(i)

sort_queue(q)
while not q.empty():
    print q.get(),

