class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 == 1:
            result = [0]
            n = n-1
        
        for i in range(1,(n//2)+1):
            result = [-1 * i] + result + [i]
        
        return result
        
