'''
   Design a stack with operations on middle element O(1) time complexity
   1) push() which adds an element to the top of stack.
   2) pop() which removes an element from top of stack.
   3) findMiddle() which will return middle element of the stack.
   4) deleteMiddle() which will delete the middle element.
'''

# IDEA IS TO USE A DOUBLY LINKED LIST
# Since an array will not support removing middle operation in O(1) time
# as we will need to move all the elements on the other half by one
# Single linked list will not work, as we won't be able to move up and down

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Stack(object):

    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

    def push(self, val):
        newNode = Node(val)
        # Since we are adding the node to the beginning of the list
        # newNode.prev will always be None
        newNode.next = self.head
        self.count += 1
        if self.count == 1:
            self.mid = newNode
        else:
            self.head.prev = newNode
            if self.count % 2 != 0:
                self.mid = self.mid.prev
        self.head = newNode

    def pop(self):
        poppedNode = self.head
        self.count -= 1
        if self.count == 0:
            self.mid = None
        if self.count % 2 == 0:
            self.mid = self.mid.next
        self.head = self.head.next
        self.head.prev = None
        return poppedNode.val

    def print_stack(self):
        if not self.head:
            return None
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next
        print '\n'

    def print_mid(self):
        print 'Mid', self.mid.val


s = Stack()
s.push(1)
s.print_stack()
s.print_mid()
s.push(2)
s.print_stack()
s.print_mid()
s.push(3)
s.print_stack()
s.print_mid()
s.push(4)
s.print_stack()
s.print_mid()
s.push(5)
s.print_stack()
s.print_mid()

print 'popped', s.pop()
s.print_stack()
s.print_mid()
print 'popped', s.pop()
s.print_stack()
s.print_mid()
print 'popped', s.pop()
s.print_stack()
s.print_mid()
print 'popped', s.pop()
s.print_stack()
s.print_mid()

