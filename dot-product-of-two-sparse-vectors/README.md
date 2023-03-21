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
