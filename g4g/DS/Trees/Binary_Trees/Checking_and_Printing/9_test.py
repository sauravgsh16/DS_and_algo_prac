class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and  self.right is None

def check_leaf_nodes(root1, root2):
    s1 = []
    s2 = []

    s1.append(root1)
    s2.append(root2)

    while (len(s1) != 0 or len(s2) != 0):

        if (len(s1) == 0 or len(s2) == 0):
            return False

        temp1 = s1.pop(-1)
        while (temp1 != None and not temp1.isLeaf()):

            if (temp1.right != None):
                s1.append(temp1.right)
            if (temp1.left != None):
                s1.append(temp1.left)
            temp1 = s1.pop(-1)

            # same for tree2
        temp2 = s2.pop(-1)
        while (temp2 != None and not temp2.isLeaf()):
            if (temp2.right != None):
                s2.append(temp2.right)
            if (temp2.left != None):
                s2.append(temp2.left)
            temp2 = s2.pop(-1)
        print temp1.val
        print temp2.val


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

check_leaf_nodes(root1, root2)