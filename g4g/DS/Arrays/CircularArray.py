import operator

class CircularList(list):
    def __getitem__(self, x):
        if isinstance(x, slice):
            return [self[x] for x in self._rangeify(x)]

        index = operator.index(x)
        try:
            return super(CircularList, self).__getitem__(index % len(self))
        except ZeroDivisionError:
            raise IndexError('list index out of range')

    def _rangeify(self, slice):
        start, stop, step = slice.start, slice.stop, slice.step
        if start is None:
            start = 0
        if stop is None:
            stop = len(self)
        if step is None:
            step = 1
        return range(start, stop, step)

'''
l = [10, 20, 30, 40, 50]
c = CircularArray(l)
print c[0]
print c[0:10]
print c[6]
'''
print CircularList(range(5))[1:10]