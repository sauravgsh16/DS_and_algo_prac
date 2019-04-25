''' Sum of all nodes of a perfect binary tree of level L '''

# METHOD 1
# Calculate the number of nodes 'n'.
# Thus sum of all leaf nodes, will be sum of first n positive integers
# Total will be sum of (leaf nodes * no of levels)


def sum_perfect_b_tree(levels):
    leafnodes = 2 ** (levels - 1)
    leaf_level_total = (leafnodes * (leafnodes + 1)) / 2 # n(n-1)/2
    return leaf_level_total * levels


print sum_perfect_b_tree(3)