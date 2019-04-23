''' Subtree with given sum in a Binary Tree '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# The idea is to traverse tree in Postorder fashion because here we have to think bottom-up.
# First calculate the sum of left subtree then right subtree and check if 
# sum_left + sum_right + cur_node = sum is satisfying the 
# condition that means any subtree with given sum exist.

def subtree_sum_util(node, specified_sum, cur_sum):

    if not node:
        cur_sum[0] = 0
        return False
    
    # Here first we go to left sub-tree,
    # then right subtree then first we
    # calculate sum of all nodes of subtree
    # having ptr as root and assign it as cur_sum
    # cur_sum = sum_left + sum_right + ptr.data
    # after that we check if cur_sum == sum

    sum_left, sum_right = [0], [0]
    x = subtree_sum_util(node.left, specified_sum, sum_left)
    y = subtree_sum_util(node.right, specified_sum, sum_right)

    cur_sum[0] = sum_left[0] + sum_right[0] + node.val

    return ((x or y) or cur_sum[0] == specified_sum)


def sum_subtree(root, specified_sum):
    cur_sum = [0]
    #return sumSubtreeUtil(root, cur_sum, specified_sum)
    return subtree_sum_util(root, specified_sum, cur_sum)

root = Node(8)
root.left = Node(5)
root.right = Node(4)
root.left.left = Node(9)
root.left.right = Node(7)
root.left.right.left = Node(1)
root.left.right.right = Node(12)
root.left.right.right.right = Node(2)
root.right.right = Node(11)
root.right.right.left = Node(3)
specified_sum = 22

print sum_subtree(root, specified_sum)