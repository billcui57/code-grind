from collections import Counter
class Solution:

    def remove_balloon(self, counter):

        for c in "balloon":
            if c not in counter:
                return False
            if counter[c] == 0:
                return False
            counter[c] -=1
        return True


    def maxNumberOfBalloons(self, text: str) -> int:

        text_counter = Counter(list(text))

        result = 0
        while self.remove_balloon(text_counter):
            result+=1
        return result

        