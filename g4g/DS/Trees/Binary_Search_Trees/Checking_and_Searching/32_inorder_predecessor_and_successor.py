''' Inorder successor and predecessor '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_pre_suc(root, node):
    if not root:
        return

    if root.val == node.val:
        if root.left is not None:
            temp = root.left
            while temp.right is not None:
                temp = temp.right
            find_pre_suc.pre = temp

        if root.right is not None:
            temp = root.right
            while temp.left is not None:
                temp = temp.left
            find_pre_suc.suc = temp
        return

    if node.val < root.val:
        find_pre_suc.suc = root
        find_pre_suc(root.left, node)
    else:
        find_pre_suc.pre = root
        find_pre_suc(root.right, node)


def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

find_pre_suc(root, root.left.right)
print 'Pre:', find_pre_suc.pre.val
print 'Suc:', find_pre_suc.suc.val
