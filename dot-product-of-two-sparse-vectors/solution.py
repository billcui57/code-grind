class SparseVector:
    def __init__(self, nums: List[int]):
        self.els = dict()
        for i,num in enumerate(nums):
            if num != 0:
                self.els[i] = num

        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for el in self.els.keys():
            if el in vec.els:
                result += self.els[el] * vec.els[el]
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)