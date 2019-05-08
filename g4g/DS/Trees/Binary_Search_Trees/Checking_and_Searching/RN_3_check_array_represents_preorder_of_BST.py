''' Check if array represents preorder traversal of BST '''


INT_MIN = -2**32

def can_represent_BST(arr):
    # Create an empty stack
    s = []

    # Initialize current root as minimum possible value
    root = INT_MIN

    for value in arr:
        # If we find a node who is on the right side
        # and is smaller than root, we return False
        if value < root:
            return False
        
        # If value is in the right subtree of the stack top,
        # Keep removing items smaller than value 
        # and make the last removed items as new root
        while len(s) > 0 and s[-1] < value:
            root = s.pop()
        
        # At this point, stack is either empty or
        # value is smaller than root, push value
        s.append(value)
    return True

arr1 = [40 , 30 , 35 , 80 , 100]
arr2 = [40 , 30 , 35 , 20 ,  80 , 100]

#for arr in arr1, arr2:
print can_represent_BST(arr1)
