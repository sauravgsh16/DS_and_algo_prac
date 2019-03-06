'''
   Find k numbers with most occurrences in the given array
'''

# Using a map to store number of occurences, with number as key and occurences as value

def mostOccurences(arr, k):
    n = len(arr)
    hash = {}
    for i in range(n):
        if arr[i] in hash:
            hash[arr[i]] += 1
        else:
            hash[arr[i]] = 1
    
    occ_arr = [None] * len(hash)
    i = 0
    for key, val in hash.iteritems():
        occ_arr[i] = (key, val)
        i += 1
    occ_arr = sorted(occ_arr, key=lambda x: x[0], reverse=True)
    occ_arr = sorted(occ_arr, key=lambda x: x[1], reverse=True)
    print occ_arr
    
    for i in range(k):
        print occ_arr[i][0],


###################################################################
# Using hash to store occurences
# Using max heap to store results

class Node(object):
    def __init__(self, val, occ):
        self.val = val
        self.occ = occ

class MaxHeap(object):
    def __init__(self):
        self.heap = []
        self.size = 0

    def _parent(self, node):
        parent = (node - 1) / 2
        if parent == -1:
            return 0
        return parent

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def insert(self, val, occ):
        nN = Node(val, occ)
        self.heap.append(nN)
        self.size += 1

        if self.size == 1:
            return
        current = self.size - 1
        while (self.heap[current].occ > self.heap[self._parent(current)].occ
            or (self.heap[current].occ == self.heap[self._parent(current)].occ) and
            self.heap[current].val > self.heap[self._parent(current)].val):
            self._swap(current, self._parent(current))
            current = self._parent(current)
    
    def is_leaf(self, pos):
        if pos >= (self.size - 1) / 2 and pos <= self.size - 1:
            return True
        return False

    def _left(self, pos):
        return 2 * pos + 1
    
    def _right(self, pos):
        return 2 * pos + 2

    def heapify(self, pos):
        if self.is_leaf(pos):
            return
        left = self._left(pos)
        right = self._right(pos)

        if self.heap[pos].occ < self.heap[left].occ or self.heap[pos].occ < self.heap[right].occ:
            if self.heap[left].occ > self.heap[right].occ or not self.heap[right]:
                self._swap(pos, left)
                self.heapify(left)
            else:
                self._swap(pos, right)
                self.heapify(right)
        elif self.heap[pos].val < self.heap[left].val or self.heap[pos].val < self.heap[right].val:
            if self.heap[left].val > self.heap[right].val or not self.heap[right]:
                self._swap(pos, left)
                self.heapify(left)
            else:
                self._swap(pos, right)
                self.heapify(right)

    def extractMax(self):
        self._swap(0, self.size - 1)
        maxElem = self.heap.pop()
        self.size -= 1
        self.heapify(0)
        return maxElem.val


# [(5, 3), (11, 2), (7, 2), (10, 1), (9, 1), (8, 1), (2, 1)]
def mostOccurencesHeap(arr, k):
    n = len(arr)
    hash = {}
    for i in range(n):
        if arr[i] in hash:
            hash[arr[i]] += 1
        else:
            hash[arr[i]] = 1

    heap = MaxHeap()
    for v, o in hash.iteritems():
        heap.insert(v, o)
    
    for _ in range(k):
        print heap.extractMax()

# mostOccurences([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4)
mostOccurencesHeap([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4)
