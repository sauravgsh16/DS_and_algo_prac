''' Sorted Linked List to Balanced Binary Tree '''

'''
   Method 1:
   1) We calculate the middle of the linkedlist and make it root.
   2) Recursively do same with left and right half.
      a) get the middle of the left half and make it left child of root
         created in step 1
      b) get middle of right half and make it right child of root created in
         step 1  
'''

'''
   Method 2:
   Here we construct trees from leaves to root.
   The idea is to insert nodes in BST in the same order as they appear in
   the Linked List, so that tree can be constructed in O(n) time complexity.
   We first count the number of node in the Linked List, say n
   We then take left n/2 nodes and recusively construct the left subtree.
   After left subtree is constructed, we allocate memory for root and link the
   left subtree with root. Finally, we recursively construct the right subtree
   and link it with root.

   While constructing the BST, we keep moving the list head pointer to next so
   that we have the appropriate pointed in each recursive calls
'''


class LinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, val):
        newNode = LinkedListNode(val)
        if not self.head:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
            newNode.prev = cur
        self.size += 1

    def print_list(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next
        print '\n'


class BinaryTree(object):

    def __init__(self, ll_data_arr):
        self.ll = LinkedList()
        for data in ll_data_arr:
            self.ll.insert(data)
        self.head = self.ll.head
        self.root = None

    def sorted_linked_list_to_BST(self):
        self.root = self.sorted_linked_list_to_BST_util(self.ll.size)

    def sorted_linked_list_to_BST_util(self, n):
        if n <= 0:
            return

        left = self.sorted_linked_list_to_BST_util(n/2)
        root = BinaryTreeNode(self.head.val)
        root.left = left

        self.head = self.head.next
        root.right = self.sorted_linked_list_to_BST_util(n - n/2 - 1)
        return root

    def _print_tree_inorder(self, root):
        if not root:
            return
        self._print_tree_inorder(root.left)
        print root.val,
        self._print_tree_inorder(root.right)

    def print_tree_inorder(self):
        self._print_tree_inorder(self.root)
        print '\n'

    def _print_tree_preorder(self, root):
        if not root:
            return
        print root.val,
        self._print_tree_preorder(root.left)
        self._print_tree_preorder(root.right)

    def print_tree_preorder(self):
        self._print_tree_preorder(self.root)
        print '\n'


bt = BinaryTree([1, 2, 3, 4, 5, 6, 7])
bt.ll.print_list()

bt.sorted_linked_list_to_BST()
bt.print_tree_inorder()
bt.print_tree_preorder()
