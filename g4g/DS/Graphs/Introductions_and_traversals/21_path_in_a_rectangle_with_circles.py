''' Path in a rectangle with circles '''

'''
   Problem statement:

   There is a m*n rectangular matrix whose top-left (start) location is (1, 1)
   and the bottom-right (end) location is (m, n). There are k circles each with
   radius r. Find if there is any path from start to end without touching any
   circles.

   Input -> m, n, k, r.
   Input also contains array, X and Y, each of length k, such that:
        (X[i], Y[i]) is the centre of the circle

   Refer: https://www.geeksforgeeks.org/path-rectangle-containing-circles/
   for more details
'''

'''
   Pythagorean theorem:
        Circle Center (a, b), radius = r
        Point (x, y)
    For the point to lie inside or on the circle:
    sqrt((a-x)**2 + (b-y)**2) <= r
'''
import math
import unittest

def ispossible(m, n, k, r, X, Y):
    # Create an array of m * n
    # Very important to create matrix this way
    rect = [[0 for _ in range(n)] for _ in range(m)]

    # Mark cells are blocked, if cell touches or within the circle
    for i in range(m):
        for j in range(n):
            for p in range(k):
                val = math.sqrt((X[p] -1 - i) ** 2 + (Y[p] -1 - j) ** 2)
                if val <= r:
                    rect[i][j] = -1


    if rect[0][0] == -1:
        return False
    
    # Now we use BFS to find if there is any possible path.
    queue = []
    rect[0][0] = 1
    queue.append((0, 0))
    
    while len(queue) > 0:
        elex, eley = queue.pop(0)

        # Discover eight adjacent nodes

        # Check top-left and mark visited
        if elex > 0 and eley > 0 and rect[elex - 1][eley - 1] == 0:
            rect[elex - 1][eley - 1] = 1
            queue.append((elex - 1, eley - 1))

        # Check top
        if elex > 0 and rect[elex - 1][eley] == 0:
            rect[elex - 1][eley] = 1
            queue.append((elex - 1, eley))
        
        # Check top-right
        if elex > 0 and eley < n - 1 and rect[elex - 1][eley  + 1] == 0:
            rect[elex - 1][eley + 1] = 1
            queue.append((elex - 1, eley + 1))
        
        # Check left
        if eley > 0 and rect[elex][eley - 1] == 0:
            rect[elex][eley - 1] = 1
            queue.append((elex, eley - 1))
        
        # Check right
        if eley < n - 1 and rect[elex][eley + 1] == 0:
            rect[elex][eley + 1] = 1
            queue.append((elex, eley + 1))
        
        # Check bottom-left
        if elex < m - 1 and eley > 0 and rect[elex + 1][eley - 1] == 0:
            rect[elex + 1][eley - 1] = 1
            queue.append((elex + 1, eley - 1))

        # Check bottom
        if elex < m - 1 and rect[elex + 1][eley] == 0:
            rect[elex + 1][eley] = 1
            queue.append((elex + 1, eley))
        
        # Check bottom-right
        if elex < m - 1 and eley < n - 1 and rect[elex + 1][eley + 1] == 0:
            rect[elex + 1][eley + 1] = 1
            queue.append((elex + 1, eley + 1))
    
    return rect[m - 1][n - 1] == 1


class TestPossible(unittest.TestCase):
    M = 5
    N = 5
    K = 2
    R = 1

    def test_1(self):
        X1 = [1, 3]
        Y1 = [3, 3]
        self.assertTrue(ispossible(self.M, self.N, self.K, self.R, X1, Y1))

    def test_2(self):
        X2 = [1, 1]
        Y2 = [2, 3]
        self.assertFalse(ispossible(self.M, self.N, self.K, self.R, X2, Y2))


if __name__ == '__main__':
    unittest.main()