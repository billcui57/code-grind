# no deque
class Node:
    def __init__(self,key):
        self.next = None
        self.prev = None
        self.key= key


class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.cache = dict()
        self.recentLocation = dict()
        
    def refresh(self, key):
        self._del(key)
        self._add(key)

    def get(self, key: int) -> int:
        # print(f"get {key}")
        if key not in self.cache:
            return -1
        
        self.refresh(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        # print(f"put {key}")

        if key in self.cache:
            self.refresh(key)
            self.cache[key]=value
            return

        if len(self.cache) >= self.capacity:
            stale_node = self.head
            self.cache.pop(stale_node.key)
            self._del(stale_node.key)

        self._add(key)
        self.cache[key] = value
    
    def _print(self):
        node = self.head
        while node is not None:
            print(node.key, node.prev, node.next)
            node = node.next

    def _del(self,key):
        # print(f"del {key}")
        node = self.recentLocation.pop(key)
        if node == self.head:
            if node.next is not None:
                self.head = node.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
        elif node == self.tail:
            if node.prev is not None:
                self.tail = node.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
        else:
            after = node.next
            prev = node.prev
            prev.next = after
            after.prev = prev
        # self._print()
    
    def _add(self,key):
        # print(f"add {key}")
        node = Node(key)
        self.recentLocation[key] = node
        if self.tail is None:
            self.tail= node
            self.head=node
        else:
            temp = self.tail
            temp.next = node
            node.prev = temp
            self.tail= node
        # self._print()

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# yes deque


from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.deque = deque()
        
    def refresh(self, key):
        self.deque.remove(key)
        self.deque.append(key)

    def get(self, key: int) -> int:
        # print(f"get {key}")
        if key not in self.cache:
            return -1
        
        self.refresh(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        # print(f"put {key}")

        if key in self.cache:
            self.refresh(key)
            self.cache[key]=value
            return

        if len(self.cache) >= self.capacity:
            stale_node = self.deque.popleft()
            self.cache.pop(stale_node)

        self.deque.append(key)
        self.cache[key] = value


    



        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)