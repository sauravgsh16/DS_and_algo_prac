''' Find repeated element which has the minimum index '''

# We use hash table to find the result
# Idea is to use a min pointer to keep track of lowest index
# We traverse from the right most side.

def find_repeated(arr):
    table = set()
    min = -1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] in table:
            min = i
        else:
            table.add(arr[i])

    if min == -1:
        print "No repeated elements"
    else:
        print arr[min]


arr = [10, 5, 3, 4, 3, 5, 6]
find_repeated(arr)
