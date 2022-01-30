def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefixProduct = {}
    prefixProduct[0] = 1
    for i in range(1, len(nums)):
        prefixProduct[i] = prefixProduct[i-1] * nums[i-1]

    suffixProduct = {}
    suffixProduct[len(nums) - 1] = 1
    for i in reversed(range(0, len(nums)-1)):
        suffixProduct[i] = suffixProduct[i+1] * nums[i+1]

    answer = [None] * len(nums)
    for i in range(0, len(nums)):
        answer[i] = prefixProduct[i] * suffixProduct[i]

    return answer
