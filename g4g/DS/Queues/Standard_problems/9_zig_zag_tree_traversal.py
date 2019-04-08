''' ZigZag Tree Traversal '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def zig_zag_traversal(root):
    if root is None:
        return
    
    # 2 stacks to traverse, current and next level
    currentLevel = []
    nextLevel = []

    # ltr when True, we traverse from left to right,
    # otherwise, traverse from right to left
    ltr = True

    currentLevel.append(root)

    while len(currentLevel) > 0:
        node = currentLevel.pop()
        print node.val,

        if ltr:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        else:
            if node.right:
                nextLevel.append(node.right)
            if node.left:
                nextLevel.append(node.left)
        
        if len(currentLevel) == 0:
            ltr = not ltr
            currentLevel, nextLevel = nextLevel, currentLevel


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
print("Zigzag Order traversal of binary tree is")
zig_zag_traversal(root)