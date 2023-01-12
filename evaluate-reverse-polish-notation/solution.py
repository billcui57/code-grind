class Solution:
    
    operators = set(["+","-","*","/"])

    def operate(self, left, right, operator):
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "*":
            return left *right
        if operator == "/":
            return int(left/right)

    def eval(self, tokens):
        el = tokens.pop()
        if el in self.operators:
            right = self.eval(tokens)
            left = self.eval(tokens)
            return self.operate(left,right, el)
        return int(el)

    def evalRPN(self, tokens: List[str]) -> int:
        result = self.eval(tokens)
        return result