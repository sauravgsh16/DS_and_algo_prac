''' Find kth largest element in BST using constant extra space '''

# Idea is to do reverse Morris Traversal

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def kth_largest_element(root, k):
    curr = root
    kLargest = None

    # Keep count of visited nodes
    count = 0

    while curr != None:
        if curr.right == None:
            # First increment count and 
            # check if k == count
            count += 1
            if k == count:
                kLargest = curr
            # Move left
            curr = curr.left
        else:
            # Find inorder successor of current node
            succ = curr.right

            while succ.left != None and succ.left != curr:
                succ = succ.left
            
            if succ.left == None:
                # Set left child of successor to current node
                succ.left = curr
                # Move curr to its right
                curr = curr.right
            
            # Restorin tree back to its original tree by removing thread
            else:
                succ.left = None
                count += 1
                if count == k:
                    kLargest = curr
                # Move cuur to its left child
                curr = curr.left
    return kLargest.val

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(10)

print kth_largest_element(root, 2)