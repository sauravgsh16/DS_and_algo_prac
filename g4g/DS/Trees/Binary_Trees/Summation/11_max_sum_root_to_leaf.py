''' Maximum sum leaf to root path in a Binary Tree '''


'''
    Solution
    1) First find the leaf node that is on the maximum sum path. In the following
       code getTargetLeaf() does this by assigning the result to *target_leaf_ref.
    2) Once we have the target leaf node, we can print the maximum sum path by
       traversing the tree. In the following code, printPath() does this.
    The main function is maxSumPath() that uses above two functions to get the complete solution.
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree(object):

    def __init__(self, root):
        self.root = root
        self.max_sum_ref = None
        self.target_leaf = None

    def getTargertLeaf(self, node, current_sum):
        if not node:
            return
        
        current_sum = current_sum + node.val

        # If this is a leaf node, and path of this node has maximum sum so far,
        # then make this node target_leaf
        if not node.left and not node.right:
            if current_sum > self.max_sum_ref:
                self.max_sum_ref = current_sum
                self.target_leaf = node
        
        self.getTargertLeaf(node.left, current_sum)
        self.getTargertLeaf(node.right, current_sum)

    def print_path(self, node):
        if not node:
            return False
        
        if node == self.target_leaf or self.print_path(node.left) or \
            self.print_path(node.right):
            print node.val,
            return True
        return False

    def max_sum_path(self):
        if not self.root:
            return 0
        self.getTargertLeaf(root, 0)
        self.print_path(self.root)
        return self.max_sum_ref


root = Node(10)
root.left = Node(-2)
root.right = Node(7)
root.left.left = Node(8)
root.left.right = Node(-4)

bt = BinaryTree(root)
max_sum= bt.max_sum_path()
print '\nMax sum ->', max_sum