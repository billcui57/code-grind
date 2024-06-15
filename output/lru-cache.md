# LRU Cache

## Link

https://leetcode.com/problems/lru-cache/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

## Solution Main Idea

Use deque (doubly linked list) to keep track of order.
Dict to point to each node via key
An actual dict to store key vals


## Code

```python
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
```
