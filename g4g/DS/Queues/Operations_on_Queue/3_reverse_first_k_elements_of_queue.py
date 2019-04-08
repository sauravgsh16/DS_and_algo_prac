''' Reverse first K elements of a Queue '''


from Queue import Queue

def reverse_k_elements(queue, k, count):
    if count >= k or queue.empty():
        return
    val = queue.get()
    reverse_k_elements(queue, k, count + 1)
    queue.put(val)

def reverse_queue(queue, k):
    count = 0
    # Reverse k elements and enQueue at the end of queue
    reverse_k_elements(queue, k, count)

    # Now pop remaining elements and put in the back of Queue
    for i in range(queue.qsize() - k):
        val = queue.get()
        queue.put(val)

def print_queue(queue):
    while not queue.empty():
        print queue.get(),

q = Queue()
for i in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    q.put(i)

reverse_queue(q, 5)
print_queue(q)