class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, root):
        self.root = root
        self.max_sum = 0
        self.target_leaf = None

    def get_target_leaf(self, node, current_sum):
        if not node:
            return
        
        current_sum = current_sum + node.val

        if not node.left and not node.right:
            if current_sum > self.max_sum:
                self.max_sum = current_sum
                self.target_leaf = node
        
        self.get_target_leaf(node.left, current_sum)
        self.get_target_leaf(node.right, current_sum)

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
        
        self.get_target_leaf(self.root, 0)
        print '\nTarget leaf', self.target_leaf.val
        self.print_path(self.root)
        return self.max_sum


root = Node(10)
root.left = Node(-2)
root.right = Node(7)
root.left.left = Node(8)
root.left.right = Node(-4)

bt = BinaryTree(root)
max_sum= bt.max_sum_path()
print '\nMax sum ->', max_sum