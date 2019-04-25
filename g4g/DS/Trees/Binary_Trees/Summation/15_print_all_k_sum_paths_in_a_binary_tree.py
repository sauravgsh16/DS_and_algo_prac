''' Print all k-sum paths in a binary tree '''

'''
   A binary tree and a number k are given. Print every path in the tree with sum
   of the nodes in the path as k.
   A path can start from any node and end at any node and must be downward only,
   i.e. they need not be root node and leaf node; and negative numbers can also 
   be there in the tree.
   Input : k = 5  
        Root of below binary tree:
           1
        /     \
      3        -1
    /   \     /   \
   2     1   4     5                        
        /   / \     \                    
       1   1   2     6    
                       
    Output :
    3 2 
    3 1 1 
    1 3 1 
    4 1 
    1 -1 4 1 
    -1 4 2 
    5 
    1 -1 5 
'''

'''
   Solution:
   1) Do a preorder traversal.
   2) Have a vector to store the paths.
   3) At each node, we check if there are any path that sums to k.
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_path(path, j):
    for i in range(j, len(path)):
        print path[i],
    print '\n'

def print_k_paths_util(node, path, specified_sum):
    if not node:
        return
    
    path.append(node.val)
    # Left traversal
    print_k_paths_util(node.left, path, specified_sum)
    # Right traversal
    print_k_paths_util(node.right, path, specified_sum)
    s = 0
    for j in range(len(path) -1, -1, -1):
        s += path[j]

        if s == specified_sum:
            print_path(path, j)
    path.pop()


def print_K_path(root, specified_sum):
    path = []
    print_k_paths_util(root, path, specified_sum)


root = Node(1)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.left = Node(1)
root.right = Node(-1)
root.right.left = Node(4)
root.right.left.left = Node(1)
root.right.left.right = Node(2)
root.right.right = Node(5)
root.right.right.right = Node(2)

specified_sum = 6
print_K_path(root, specified_sum)
