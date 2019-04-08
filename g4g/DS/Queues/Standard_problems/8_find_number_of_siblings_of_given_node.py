''' Find the number of siblings of a given node in n-ary tree '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []


def number_of_siblings(root, x):
    if not root:
        return
    
    q = []
    q.append(root)

    while len(q) > 0:
        node = q.pop(0)

        for child in node.children:

            if child.val == x:
                return len(node.children) - 1
            q.append(child)


root = Node(50)  
(root.children).append(Node(2))  
(root.children).append(Node(30))  
(root.children).append(Node(14))  
(root.children).append(Node(60))  
(root.children[0].children).append(Node(15))  
(root.children[0].children).append(Node(25))  
(root.children[0].children[1].children).append(Node(70))  
(root.children[0].children[1].children).append(Node(100))  
(root.children[1].children).append(Node(6))  
(root.children[1].children).append(Node(1))  
(root.children[2].children).append(Node(7))  
(root.children[2].children[0].children).append(Node(17))  
(root.children[2].children[0].children).append(Node(99))  
(root.children[2].children[0].children).append(Node(27))  
(root.children[3].children).append(Node(16))

x = 100

print number_of_siblings(root, x)