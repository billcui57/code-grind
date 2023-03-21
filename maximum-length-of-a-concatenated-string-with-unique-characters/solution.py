class Solution1:
    def maxLength(self, arr: List[str]) -> int:
        return self.dfs(arr,-1,"")
    
    def dfs(self, arr, pos, result):
        if len(set(result)) < len(result):
            return 0
        
        best_len = len(result)
        for i in range(pos+1, len(arr)):
            best_len = max(best_len, self.dfs(arr, i, result+arr[i]))
        return best_len

class Solution2:
    def maxLength(self, arr: List[str]) -> int:
        return self.dfs(arr,-1,"")

    def get_len(self, bits):
        return bits >> 26

    def get_set(self, bits):
        return bits & ((1<<26)-1)

    def pack(self, length, char_set):
        return (length << 26) | char_set
    
    def word_to_bitwise_uniq(self, string):
        
        char_set = 0
        char_len = 0

        for c in string:
            char_index = ord(c) - ord("a")
            mask = (1 <<  char_index)
            if char_set & mask > 0:
                return 0
            char_set = char_set | mask
            char_len += 1
        return self.pack(char_len,char_set)
    
    def maxLength(self, arr):
        aug = [self.word_to_bitwise_uniq(e) for e in arr]
        return self.dfs(aug, -1, 0)
    
    def dfs(self, arr, pos, result):
        char_set =  self.get_set(result)
        char_len = self.get_len(result)

        best = char_len

        for i in range(pos+1, len(arr)):
            
            new_chars_set = self.get_set(arr[i])
            if new_chars_set & char_set:
                continue
            
            new_chars_len = self.get_len(arr[i])

            res_chars_set = new_chars_set | char_set
            res_chars_len = new_chars_len + char_len
            best = max(best, self.dfs(arr, i, self.pack(res_chars_len,res_chars_set )))
        return best
        