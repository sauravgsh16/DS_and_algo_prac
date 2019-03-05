'''
   Kth Smallest/Largest Element in Unsorted Array

   Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
   Output: 7
'''

# METHOD 1 : O(nlogn)
# Sort and return index

def kthelement(arr, k):
    arr.sort()
    return arr[k-1]
# *****************************************************************************

# METHOD 2:
# Create a min heap and call extractMin k times.

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

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        if self.size == 1:
            return
        current = self.size - 1
        while self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _left(self, node):
        left = 2 * node + 1
        if left > self.size:
            return -1
        return left
    
    def _right(self, node):
        right = 2 * node + 2
        if right > self.size:
            return -1
        return right

    def _is_leaf(self, node):
        if node >= (self.size - 1) / 2 and node <= self.size-1:
            return True
        return False

    def heapify(self, node):
        if self._is_leaf(node):
            return
        left = self._left(node) if self._left(node) != -1 else False
        right = self._right(node) if self._right(node) != -1 else False
        if self.heap[node] > self.heap[left] or self.heap[node] > self.heap[right]:
            if self.heap[left] < self.heap[right] or not self.heap[right]:
                self._swap(node, left)
                self.heapify(left)
            else:
                self._swap(node, right)
                self.heapify(right)
    
    def extractMin(self):
        self._swap(0, self.size-1)
        min = self.heap.pop()
        self.size -= 1
        self.heapify(0)
        return min


def kthSmallest(arr, k):
    heap = MinHeap()
    for elem in arr:
        heap.insert(elem)
    smallest = -1
    for i in range(k):
        smallest = heap.extractMin()
    return smallest

# *****************************************************************************

# METHOD 3: QuickSelect

# NEED TO IMPLEMENT
# ******************************************************************************

if __name__ == '__main__':
    print kthSmallest([12, 3, 5, 7, 19], 2)
    
