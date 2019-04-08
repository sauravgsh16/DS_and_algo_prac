''' Interleave the fisrt half with of the queue with second half '''

from Queue import Queue

# MY METHOD
def interleave(q):
    mid = q.qsize() / 2
    s1 = []
    s2 = []

    while q.qsize() != mid:
        s1.append(q.get())
    while not q.empty():
        s2.append(q.get())
    
    while len(s1) != 0 or len(s2) != 0:
        q.put(s1.pop(0))
        q.put(s2.pop(0))


# METHOD GIVEN

def interleave_official(q):

    # To check the even number of elements  
    if (q.qsize() % 2 != 0):  
        print("Input even number of integers.") 
  
    # Initialize an empty stack of int type  
    s = [] 
    halfSize = int(q.qsize() / 2)  
  
    # put first half elements into  
    # the stack queue:16 17 18 19 20,  
    # stack: 15(T) 14 13 12 11 
    for i in range(halfSize): 
        s.append(q.get())
  
    # enqueue back the stack elements  
    # queue: 16 17 18 19 20 15 14 13 12 11  
    while len(s) != 0:  
        q.put(s.pop())
  
    # dequeue the first half elements of  
    # queue and enqueue them back  
    # queue: 15 14 13 12 11 16 17 18 19 20 
    for i in range(halfSize): 
        q.put(q.get())
  
    # Again put the first half elements into  
    # the stack queue: 16 17 18 19 20, 
    # stack: 11(T) 12 13 14 15  
    for i in range(halfSize): 
        s.append(q.get())
  
    # interleave the elements of queue and stack  
    # queue: 11 16 12 17 13 18 14 19 15 20  
    while len(s) != 0:  
        q.put(s.pop())  
        q.put(q.get())


def print_queue(queue):
    while not queue.empty():
        print queue.get(),
    print '\n'

q = Queue()
for i in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
    q.put(i)

interleave(q)
print_queue(q)

for i in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
    q.put(i)
interleave_official(q)
print_queue(q)
