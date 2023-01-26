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