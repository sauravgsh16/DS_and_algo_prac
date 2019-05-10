''' Sum of k smallest elements of a BST '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_k_smallest_nodes_util(root, count, k):
    if not root:
        return 0
    if count[0] > k:
        return 0

    res = sum_k_smallest_nodes_util(root.left, count, k)
    if count[0] >= k:
        return res

    res += root.val
    count[0] += 1

    if count[0] >= k:
        return res
    return res + sum_k_smallest_nodes_util(root.right, count, k)


def sum_k_smallest_nodes(root, k):
    count = [0]
    return sum_k_smallest_nodes_util(root, count, k)


root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.left.left = Node(1)


print sum_k_smallest_nodes(root, 6)
