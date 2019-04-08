''' Constuct a Binary Tree from it's Linked Link representation '''

class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class BinaryTreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Conversion(object):

    def __init__(self):
        self.head = None
        self.root = None

    def push(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def linked_list_to_binary_tree(self):
        if not self.head:
            return

        queue = []

        self.root = BinaryTreeNode(self.head.val)
        queue.append(self.root)

        cur = self.head.next
        while cur:
            parent = queue.pop(0)
            leftChild = None
            rightChild = None

            leftChild = BinaryTreeNode(cur.val)
            queue.append(leftChild)
            cur = cur.next
            if cur:
                rightChild = BinaryTreeNode(cur.val)
                queue.append(rightChild)
                cur = cur.next
            
            parent.left = leftChild
            parent.right = rightChild

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print root.val,
            self.inorder_traversal(root.right)


conv = Conversion()
conv.push(36)
conv.push(30)
conv.push(25)
conv.push(15)
conv.push(12)
conv.push(10)

conv.linked_list_to_binary_tree()
conv.inorder_traversal(conv.root)

