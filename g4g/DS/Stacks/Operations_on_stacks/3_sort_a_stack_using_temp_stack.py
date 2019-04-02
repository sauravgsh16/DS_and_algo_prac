''' Sort a stack using a temporary stack '''

class Stack(object):
    def __init__(self):
        self.main = []
        self.temp = []

    def push_main(self, val):
        self.main.append(val)
    
    def push_temp(self, val):
        self.temp.append(val)

    def pop_main(self):
        return self.main.pop()

    def pop_temp(self):
        return self.temp.pop()

    def top_temp(self):
        return self.temp[-1]

    def sort(self):
        while len(self.main) != 0:
            top_m = self.pop_main()
            while len(self.temp) != 0 and self.top_temp() > top_m:
                top_t = self.pop_temp()
                self.push_main(top_t)
            self.push_temp(top_m)
        return self.temp

s = Stack()
s.push_main(98)
s.push_main(92)
s.push_main(34)
s.push_main(31)
s.push_main(23)
s.push_main(3)
print s.sort()
