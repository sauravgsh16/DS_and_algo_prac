''' Construct a Binary tree from it's Linked List representation '''

class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class LinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Conversion(object):
    def __init__(self):
        self.head = None
        self.root = None

    def push(self, val):
        newNode = LinkedListNode(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def convert_linked_list_to_binary_tree(self):
        if not self.head:
            return
        
        self.root = BinaryTreeNode(self.head.val)
        current = self.head.next
        q = []
        q.append(self.root)
        while current:
            leftNode = None
            rightNode = None
            # Parent for the left and right node
            parent = q.pop(0)

            leftNode = BinaryTreeNode(current.val)
            q.append(leftNode)
            current = current.next
            if current:
                rightNode = BinaryTreeNode(current.val)
                q.append(rightNode)
                current = current.next

            parent.left = leftNode
            parent.right = rightNode
    
    def _inorder_traversal_util(self, root):
        if not root:
            return
        self._inorder_traversal_util(root.left)
        print root.val,
        self._inorder_traversal_util(root.right)

    def inorder_traversal(self):
        self._inorder_traversal_util(self.root)


c = Conversion()
c.push(5)
c.push(4)
c.push(3)
c.push(2)
c.push(1)

c.convert_linked_list_to_binary_tree()
c.inorder_traversal()
        

