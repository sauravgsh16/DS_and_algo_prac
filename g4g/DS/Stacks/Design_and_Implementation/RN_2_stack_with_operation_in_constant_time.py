'''
   Special Stack implementation with push(), pop(), isEmpty(), isFull()
   and additional operation getMin(), all in O(1) time
'''

class SpecialStack(object):
    
    def __init__(self):
        self.main = []
        self.aux = []
    
    def push(self, val):
        self.main.append(val)
        self._update_aux_stack(val)
    
    def _update_aux_stack(self, val):
        if len(self.aux) != 0:
            top = self.aux.pop()
            if top > val:
                self.aux.append(top)
                self.aux.append(val)
            else:
                self.aux.append(top)
        else:
            self.aux.append(val)

    def pop(self):
        main_top = self.main.pop()
        aux_top = self.aux.pop()
        if main_top != aux_top:
            self.aux.append(aux_top)
        return main_top

    def getMin(self):
        val = self.aux.pop()
        self.aux.append(val)
        print val
