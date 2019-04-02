''' Reverse individual words '''

# Simple:
# Generate all words separated by space.
# One by one reverse words and print them separated by space

# Space efficient
class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0


line = 'geeks for geeks'
def reverse(line, s):
    for i in range(len(line)):
        if line[i] != ' ':
            s.push(line[i])
        else:
            while not s.isEmpty():
                ele = s.pop()
                print ele,
            print " ",
    # Since there may not be space in the end of the line
    while not s.isEmpty():
        ele = s.pop()
        print ele,

s = Stack()
reverse(line, s)