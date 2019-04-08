''' Reverse an Queue '''


from Queue import Queue

def reverse_queue(queue):
    stack = []
    while not queue.empty():
        stack.append(queue.get())
    while len(stack) != 0:
        val = stack.pop()
        queue.put(val)
    return queue


def print_queue(queue):
    while not queue.empty():
        print queue.get(),


queue = Queue()
for i in range(1, 6):
    queue.put(i)
queue = reverse_queue(queue)

print_queue(queue)