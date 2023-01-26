import re
class Solution:
    def myAtoi(self, s: str) -> int:
        
        regexResult = re.search(r"^[ ]*[-+]?[0-9]+",s)

        if regexResult == None:
            return 0


        return max(min((1 << 31) - 1, int(regexResult.group())), -1 * (1 << 31))



        


