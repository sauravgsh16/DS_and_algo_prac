class HeapNode(object):
    ''' Heap Node '''
    def __init__(self, val, rn, cn):
        self.val = val
        self.rn = rn
        self.cn = cn


class MinHeap(object):
    ''' Min Heap '''
    def __init__(self):
        self.heap = []
        self.size = 0

    def _parent(self, idx):
        parent = (idx - 1) / 2
        if parent <= 0:
            return 0
        return parent

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def insert(self, val, rn, cn):
        newNode = HeapNode(val, rn, cn)
        self.heap.append(newNode)
        self.size += 1

        if self.size == 1:
            return
        current = self.size - 1
        while self.heap[current].val < self.heap[self._parent(current)].val:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def peek(self):
        return self.heap[0]

    def _is_leaf(self, pos):
        if pos > ((self.size - 1) / 2) and pos <= self.size - 1:
            return True
        return False

    def _left_child(self, pos):
        left = 2 * pos + 1
        if left <= self.size - 1:
            return left
        return -1

    def _right_child(self, pos):
        right = 2 * pos + 2
        if right <= self.size - 1:
            return right
        return -1

    def _heapify(self, pos):
        if self._is_leaf(pos):
            return
        left = self._left_child(pos)
        right = self._right_child(pos)

        if left != -1 and right != -1:
            if self.heap[pos].val > self.heap[left].val or\
                self.heap[pos].val > self.heap[right].val:
                if self.heap[left].val < self.heap[right].val:
                    self._swap(pos, left)
                    self._heapify(left)
                else:
                    self._swap(pos, right)
                    self._heapify(right)
        elif left != -1:
            if self.heap[pos].val > self.heap[left].val:
                self._swap(pos, left)
                self._heapify(left)

    def replace(self, val, rn, cn):
        newNode = HeapNode(val, rn, cn)
        self.heap[0] = newNode
        self._heapify(0)


def find_kth_smallest(arr, n, k):
    # Insert first row in MinHeap
    minHeap = MinHeap()
    for cn, val in enumerate(arr[0]):
        minHeap.insert(val, 0, cn) # rn is 0 as it's the first row
    
    # Now we need to check the root value of min heap.
    # We replace the value of the min heap with the next value in the same
    # column as that of the root node.
    # We repeat this k times
    for _ in range(k):
        root = minHeap.peek()
        rn = root.rn + 1
        cn = root.cn
        try:
            minHeap.replace(arr[rn][cn], rn, cn)
        except IndexError:
            minHeap.replace(2**32, rn, cn)

    return root.val

arr = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [24, 29, 37, 48],
    [32, 33, 39, 50]
]

arr2 = [
    [16, 28, 60, 64],
    [22, 41, 63, 91],
    [27, 50, 87, 93],
    [36, 78, 87, 94]
]

# find_kth_smallest(arr, 15)

#1
#4
#16 28 60 64 22 41 63 91 27 50 87 93 36 78 87 94 
#3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        k = int(input())
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[c]
                c+=1
        print(find_kth_smallest(matrix, n[0], k))