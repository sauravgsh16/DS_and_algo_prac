''' Implementation of a LRU cache '''


class Node(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return '{0}: {1}'.format(self.key, self.val)

class LRUCache(object):

    def __init__(self, capacity):
        self.head = None
        self.rear = None
        self.hash = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        node = self.hash.get(key)
        if not node:
            return -1
        if node == self.head:
            return node.val
        
        self.remove(node)
        self.set_head(node)
        return node.val

    def set(self, key, val):
        node = self.hash.get(key)
        if node:
            node.val = val
            
            if self.head != node:
                self.remove(node)
                self.set_head(node)
        else:
            newNode = Node(key, val)
            if self.size == self.capacity:
                del self.hash[self.rear.key]
                self.remove(self.rear)
            self.set_head(newNode)
            self.hash[key] = newNode

    def set_head(self, node):
        if not self.head:
            self.head = self.rear = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.size += 1

    def remove(self, node):
        if not self.head:
            return
        
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        if not node.next and not node.prev:
            self.head = self.rear = None

        if self.rear == node:
            self.rear = node.next
            self.rear.prev = None
        self.size -= 1
        return node

    def print_cache(self):
        cur = self.head
        while cur:
            print '{} ->'.format(cur)
            cur = cur.prev
        print None


lru = LRUCache(5)
lru.set('a', 10)
lru.set('b', 20)
lru.set('c', 30)
lru.set('d', 40)
lru.set('e', 50)

print lru.get('a')
lru.print_cache()
lru.set('f', 60)
lru.print_cache()
