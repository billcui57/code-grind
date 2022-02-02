class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        local_max = 0
        
        global_max = -inf
        
        for i in range(0, len(nums)):
            local_max = max(nums[i], local_max + nums[i])
            if local_max > global_max:
                global_max = local_max
        
        return global_max