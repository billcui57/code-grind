def containsDuplicate(self, nums: List[int]) -> bool:
    seenNums = {}

    for num in nums:
        if num not in seenNums:
            seenNums[num] = 1
        else:
            seenNums[num] += 1

    for num in seenNums.values():
        if num >= 2:
            return True

    return False
