''' Swapping nodes without swapping data '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return self

    def print_linked_list(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next
    
    def swap(self, x, y):
        if x == y:
            return
        
        prev_x = prev_y = None
        cur_x = cur_y = None
        cur = self.head
        while cur and not (cur_x and cur_y):
            if cur.val == x or cur.val == y:
                if cur.val == x:
                    cur_x = cur
                    if not cur_y:
                        prev_y = cur
                else:
                    cur_y = cur
                    if not cur_x:
                        prev_x = cur
            else:
                if not cur_x:
                    prev_x = cur
                if not cur_y:
                    prev_y = cur
            cur = cur.next
        # Check if prev of any found node is None
        if not prev_x:
            self.head = cur_y
        else:
            prev_x.next = cur_y
        if not prev_y:
            self.head = cur_x
        else:
            prev_y.next = cur_x
        temp = cur_x.next
        cur_x.next = cur_y.next
        cur_y.next = temp
        

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
ll.print_linked_list()
ll.swap(3, 4)
print '\n'
ll.print_linked_list()