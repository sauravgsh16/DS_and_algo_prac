'''
   Replace each node in binary tree with the sum
   of it's predecessor and successor 
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_inorder_travesal(root, arr):
    if not root:
        return
    find_inorder_travesal(root.left, arr)
    arr.append(root.val)
    find_inorder_travesal(root.right, arr)

def replace_val_by_sum(root, arr, i):
    if not root:
        return
    replace_val_by_sum(root.left, arr, i)
    root.val = arr[i[0] - 1] + arr[i[0] + 1]
    i[0] += 1
    replace_val_by_sum(root.right, arr, i)

def main(root):
    arr = [0]
    find_inorder_travesal(root, arr)
    arr.append(0)
    i = [1]
    replace_val_by_sum(root, arr, i)
    arr = []
    find_inorder_travesal(root, arr)
    for i in arr:
        print i,


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
main(root)