class Solution:

    def dfs(self, digits, build, map,result):
        if len(digits) == 0:
            if build != "":
                result.append(build)
            return
        front = digits.pop()
        letters = map[front]
        for letter in letters:
            self.helper(digits, build+letter, map, result)
        digits.append(front)


    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(reversed(digits))

        map = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        build = ""
        result = []
        self.dfs(digits, build, map, result)
        return result


