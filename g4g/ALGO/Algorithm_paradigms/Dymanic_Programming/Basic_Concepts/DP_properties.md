## OPTIMAL SUBSTRUCTURE PROPERTY

Two of the main properties of problem that suggest that a given problem can be
solved using Dynamic Programming are:
1) `Overlapping Subproblems`
2) `Optimal Substructure`

### Overlapping Subproblems
Like `Divide and Conquer`, DP combines solutions of subproblems. DP is mainly
used when solutions of same subproblems are needed again and again.
In DP, computed solutions are stored in a table so that these don't have to be
recomputed.
DP is not useful when there are no common subproblems. eg: Binary Search

eg: When subproblems are recomputed again and again

```py

def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)
```
For `fib(5)` we have a recursion tree as:
```
                   fib(5)
              /              \
          fib(4)              fib(3)
        /       \              /      \
     fib(3)     fib(2)       fib(2)   fib(1)
    /    \       /    \       /    \
 fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
 /    \
fib(1) fib(0)
```
from above we see that fib(3) is called 2 times, and so on
Thus, we employ two ways to store the values so that these values can be reused.
1) `Memoization`
2) `Tabulation`

The above methods are discussed in other file.

### Optimal Substructure
A given problem has `Optimal substructure` property if optimal solution of the
given problem can be obtained by using optimal solutions of its subproblems

eg:
The `shortest path problem` has following optimal substructure property:

If a node lies in the shortest path from source 'u' to destination 'v', then
the shortest path from `'u' to 'v'` is a combination od shortest path from
`'u' to 'x'` and the shortest path from `'x' to 'v'`.
The `Floyd-Warshall` and `Bellman-Ford` are typical examples of DP.

On the other hand, `longest path` problem doesn't have an optimal substructure.