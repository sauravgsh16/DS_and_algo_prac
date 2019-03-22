'''
   Segregate even and odd nodes

   Input: 17->15->8->12->10->5->4->1->7->6->NULL
   Output: 8->12->10->4->6->17->15->5->1->7->NULL
'''

class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        self.size += 1
    
    def segregate_list_method_1(self):
        # We traverse to find the end of the list.
        # Then for every odd node, we push the node to the end
        last = self.head
        while last.next:
            last = last.self
        
        cur = self.head
        while cur != last:
            
