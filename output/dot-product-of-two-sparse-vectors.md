# Dot Product of Two Sparse Vectors

## Link
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/

## Where
Leetcode

## Difficulty
Medium

## Description
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

## Solution Main Idea
Keep track of only non zero elements with dict


## Code

```python
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
```
