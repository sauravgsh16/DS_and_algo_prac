'''
   Write a function to get the intersection point of two Linked Lists.
   There are two singly linked lists in a system. By some programming error,
   the end node of one of the linked list got linked to the second list,
   forming an inverted Y shaped list.
   Write a program to get the point where two linked list merge.
'''

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

# METHOD 1:
# Using two for loops

# METHOD 2:
# Using a hash table to store visited nodes.
# We traverse the first and store all the node.
# Then we traverse the second and check if node is present in hash table.

# METHOD 3:
def find_intersection_pt1(first, second):
    # Get length of fisrt - C1 and second C2
    # diff = abs(C1 - C2)
    # Now traverse longer list to 'diff'
    # Now both list can be traversed simulatenously and checked if node are same
    f = first.head
    s = second.head
    c1 = c2 = 0
    while f.next:
        c1 += 1
        f = f.next
    
    while s.next:
        c2 += 1
        s = s.next
    
    d = abs(c1-c2)
    cur_f = first.head
    cur_s = second.head
    if c1 > c2:
        cur_f = traverse(cur_f, d)
    else:
        cur_s = traverse(cur_s, d)
    while cur_f != cur_s and (cur_f or cur_s):
        cur_f = cur_f.next
        cur_s = cur_s.next
    
    print cur_f.val
    

def traverse(cur, d):
    for _ in range(d):
        cur = cur.next
    return cur


# METHOD 4:
# Form any of the two list into a circular list
# The problem then becomes about finding the start point of the loop.
def find_intersection_pt2(first, second):
    # Creating a loop for second
    # Ideally, we cannot use a tail node, and need to keep track of end node
    # So that we can revert it back to original
    print second
    second.tail.next = second.head
    first.print_linked_list()


n1 = Node('1')
n2 = Node('2')
n3 = Node('3')
n4 = Node('4')
n5 = Node('5')
n6 = Node('6')

l1 = LinkedList()
l1.head = n1
l1.head.next = n2
l1.head.next.next = n3
l1.head.next.next.next = n5
l1.head.next.next.next.next = n6

l2 = LinkedList()
l2.head = n4
l2.head.next = n5

l1.print_linked_list()
print '\n'
l2.print_linked_list()
print '\n'
find_intersection_pt1(l1, l2)
find_intersection_pt2(l1, l2)