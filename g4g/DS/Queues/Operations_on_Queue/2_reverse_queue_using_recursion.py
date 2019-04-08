''' Reverse Queue using Recursion '''

from Queue import Queue

def reverse_queue(queue):
    if queue.empty():
        return
    val = queue.get()
    reverse_queue(queue)
    queue.put(val)

def print_queue(queue):
    while not queue.empty():
        print queue.get(),


queue = Queue()
for i in range(1, 6):
    queue.put(i)

reverse_queue(queue)
print_queue(queue)