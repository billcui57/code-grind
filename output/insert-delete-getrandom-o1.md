# Insert Delete GetRandom O(1)

## Link

https://leetcode.com/problems/insert-delete-getrandom-o1/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

## Solution Main Idea

Have indices dict
Have unusedIndices set
Have values arr

remove is avg O(1) cuz we keep trying for indices that are not in unusedIndices


## Code

```python
class RandomizedSet:

    def __init__(self):
        self.indices = dict()
        self.unusedIndices = set()
        self.values=[]
        

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        if len(self.unusedIndices) > 0:
            unused_index = self.unusedIndices.pop()
            self.values[unused_index] = val
            self.indices[val] = unused_index
        else:
            self.values.append(val)
            self.indices[val] = len(self.values)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        index = self.indices[val]
        self.unusedIndices.add(index)
        self.indices.pop(val)
        return True

        

    def getRandom(self) -> int:
        while True:
            index = random.randrange(len(self.values))
            if index not in self.unusedIndices:
                break
        return self.values[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```
