''' Kth Smallest element using constant extra space '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_kth_smallest(root, k):
    curr = root
    kth_smallest = None

    count = 0
    while curr != None:
        if curr.left is None:
            count += 1
            if count == k:
                kth_smallest = curr
            curr = curr.right
        else:
            pre = curr.left
            while pre.right != None and pre.right != curr:
                pre = pre.right
            
            if pre.right == None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                count += 1

                if count == k:
                    kth_smallest = curr
                curr = curr.right
    return kth_smallest.val


root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(10)

print find_kth_smallest(root, 5)