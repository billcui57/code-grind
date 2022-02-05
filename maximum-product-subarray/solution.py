class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        local_min = [1] * len(nums)
        
        local_max = [1] * len(nums)
    
        
        local_min[0] = nums[0]
        local_max[0] = nums[0]
        
        total_max = -inf
        
        for i in range(1, len(nums)):
            
            if nums[i] >=0 :

                local_max[i] = max( local_max[i-1] * nums[i] , nums[i]) 

                local_min[i] = min( local_min[i-1] * nums[i] , nums[i])

            else:

                local_max[i] = max (local_min[i-1] * nums[i], nums[i])

                local_min[i] = min (local_max[i-1] * nums[i], nums[i])
            
            
            if local_max[i] > total_max:
                total_max = local_max[i]
        
        return max(local_max[0], total_max)
        
        
        
        
        
        
        
        
        
               
        