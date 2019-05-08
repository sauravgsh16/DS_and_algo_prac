''' Find the k-th smallest element in a BST '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

val = None
def find_kth_smallest(root, k):
    global val
    if not root:
        return k

    newK = find_kth_smallest(root.left, k)
    if newK > 0:
        val = root.val
        return find_kth_smallest(root.right, newK-1)
    else:
        return k

root = Node(40)
root.left = Node(20)
root.right = Node(50)
root.left.left = Node(10)
root.left.right = Node(30)

find_kth_smallest(root, 2)
print val