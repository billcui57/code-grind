# Insert Delete GetRandom O(1) - Duplicates allowed

## Link

https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/

## Where

Leetcode

## Difficulty

Hard

## Description

RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.

Implement the RandomizedCollection class:

RandomizedCollection() Initializes the empty RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of the same values the multiset contains.
You must implement the functions of the class such that each function works on average O(1) time complexity.

Note: The test cases are generated such that getRandom will only be called if there is at least one item in the RandomizedCollection.

## Solution Main Idea

Same as insert-delete-getrandom-o1 but use dict of array for indices


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
