''' Check if the sorted subsequence exists in a BST '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_seq_exists_util(root, seq, index):
    if not root:
        return
    check_seq_exists_util(root.left, seq, index)
    if index[0] < len(seq):
        if root.val == seq[index[0]]:
            index[0] += 1
    check_seq_exists_util(root.right, seq, index)


def check_sequence_exists(root, seq):
    index = [0]
    check_seq_exists_util(root, seq, index)

    if index[0] == len(seq):
        return True
    return False


root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(10)

seq1 = [2, 3, 4]
seq2 = [2, 3, 5]
print check_sequence_exists(root, seq1)
print check_sequence_exists(root, seq2)
