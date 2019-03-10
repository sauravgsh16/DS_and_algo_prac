'''
   Sort an array according to absolute difference with given value

   Given an array of n distinct elements and a number x, arrange array elements
   according to the absolute difference with x, i. e., element having minimum 
   difference comes first and so on.
   Note : If two or more elements are at equal distance arrange them in same 
   sequence as in the given array

    Input : arr[] : x = 7, arr[] = {10, 5, 3, 9, 2}
    Output : arr[] = {5, 9, 10, 3, 2}
    Explanation:
    7 - 10 = 3(abs)
    7 - 5 = 2
    7 - 3 = 4 
    7 - 9 = 2(abs)
    7 - 2 = 5
    So according to the difference with X, 
    elements are arranged as 5, 9, 10, 3, 2.
'''

# Implementation in geeksforgeeks says it needs a self balancing binary tree as Data Structure.
 
# ****************

# Trying implementation using a min heap.

class Node(object):
    def __init__(self, diff, val):
        self.diff = diff
        self.val = val


class MinHeap(object):

    def __init__(self):
        self.heap = []
        self.size = 0

    def _parent(self, node):
        parent = (node - 1) // 2
        if parent == -1:
            return 0
        return parent

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def insert(self, diff, val):
        nN = Node(diff, val)
        self.heap.append(nN)
        self.size += 1
        if self.size == 1:
            return
        current =  self.size - 1
        while self.heap[current].diff < self.heap[self._parent(current)].diff:
            self._swap(current, self._parent(current))
            current = self._parent(current)


arr = [10, 5, 3, 8, 2]
heap = MinHeap()
for i in arr:
    diff = abs(7 - i)
    heap.insert(diff, i)

for i in heap.heap:
    print i.val