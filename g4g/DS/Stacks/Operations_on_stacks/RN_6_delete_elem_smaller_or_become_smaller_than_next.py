''' Delete array elements which are smaller than next or become smaller '''

'''
   Input       : arr[] = { 3, 100, 1 }
              k = 1
Output      : 100, 1
Explanation : arr[0] < arr[1] means 3 is less than
              100, so delete 3

Input       : arr[] = {20, 10, 25, 30, 40}
              k = 2
Output      : 25 30 40
Explanation : First we delete 10 because it follows
              arr[i] < arr[i+1]. Then we delete 20
              because 25 is moved next to it and it
              also starts following the condition.

Input       : arr[] = { 23, 45, 11, 77, 18}
              k = 3
Output      : 77, 18
Explanation : We delete 23, 45 and 11 as they follow  
              the condition arr[i] < arr[i+1]
'''


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()


def delete_elements(arr, k):
    s = Stack()
    s.push(arr[0])
    count = 0
    top = 0
    for i in range(1, len(arr)):
        while len(s.stack) != 0 and count < k and s.stack[top] < arr[i]:
            s.pop()
            count += 1
            top -= 1
        s.push(arr[i])
        top += 1
    return s.stack

arr = [23, 45, 11, 77, 18]
print delete_elements(arr, 4)