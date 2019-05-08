''' Count pairs whose sum equals to given value in 2 given BSTs '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Trick is to traverse one tree in inorder and traverse other tree in reverse inorder. 
# If sum of nodes == given val, then increment count
# Else if val > sum, then move to inorder successor of BST1
# Else if val < sum, then move to inorder predecessor in BST2

def count_pairs(r1, r2, x):
    if not r1 or not r2:
        return 0
    count = 0
    stack1 = []
    stack2 = []

    while True:
        while r1 is not None:
            stack1.append(r1)
            r1 = r1.left

        while r2 is not None:
            stack2.append(r2)
            r2 = r2.right
       
        if len(stack1) == 0 or len(stack2) == 0:
            break

        top1 = stack1[-1]
        top2 = stack2[-1]
        if (top1.val + top2.val) == x:
            count += 1
            stack1.pop()
            stack2.pop()
            r1 = top1.right
            r2 = top2.left
        elif (top1.val + top2.val) > x:
            stack2.pop()
            r2 = top2.left
        else:
            stack1.pop()
            r1 = top1.right
    return count

root1 = Node(5)
root1.left = Node(3)
root1.right = Node(7)
root1.left.left = Node(2)
root1.left.right = Node(4)
root1.right.left = Node(6)
root1.right.right = Node(8)

root2 = Node(10)
root2.left = Node(6)
root2.right = Node(15)
root2.left.left = Node(3)
root2.left.right = Node(8)
root2.right.left = Node(11)
root2.right.right = Node(18)

print count_pairs(root1, root2, 16)
