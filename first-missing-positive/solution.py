class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # missing pos integer must be in range [1,n]

        nums.append(0)
        N= len(nums)
        for i in range(N): #delete those useless elements
            if nums[i]<0 or nums[i]>n:
                nums[i]=0
                
        for i in range(N): #use the index as the hash to record the frequency of each number
            nums[nums[i]%N]+=N
        for i in range(1,N):
            if nums[i]//N==0:
                return i
        return N


            

                
    



