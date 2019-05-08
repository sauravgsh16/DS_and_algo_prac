''' Get median of a BST in O(n) time and O(1) space '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_count_and_traverse_morris_traversal(root, count, traversal):
    curr = root
    pre = None

    while curr != None:
        if curr.left is None:
            traversal.append(curr.val)
            count[0] += 1
            curr = curr.right
        else:
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right
            
            if pre.right == None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                traversal.append(curr.val)
                count[0] += 1
                curr = curr.right


def get_median(root):
    if not root:
        return 0
    count = [0]
    traversal = []
    get_count_and_traverse_morris_traversal(root, count, traversal)
    if count[0] % 2 != 0:
        median = traversal[count[0]/2]
    else:
        median = (traversal[count[0]/2] + traversal[count[0]/2 - 1]) / 2
    return median


root1 = Node(6)
root1.left = Node(3)
root1.right = Node(8)
root1.left.left = Node(1)
root1.left.right = Node(4)
root1.right.left = Node(7)

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.left.left = Node(1)

print get_median(root)
print get_median(root1)