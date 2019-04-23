''' Sum of nodes at k-th level in a tree represented as string '''

# Input : tree = "(0(5(6()())(4()(9()())))(7(1()())(3()())))" 
#        k = 2
# Output : 14

def get_kth_sum(tree, k):
    level = -1
    kth_sum = 0
    for i in range(len(tree)):
        if tree[i] == '(':
            level += 1
        elif tree[i] == ')':
            level -= 1
        else:
            if level == k:
                kth_sum += int(tree[i])
    
    return kth_sum


tree = '(0(5(6()())(4()(9()())))(7(1()())(3()())))'
k = 2
print get_kth_sum(tree, 2)