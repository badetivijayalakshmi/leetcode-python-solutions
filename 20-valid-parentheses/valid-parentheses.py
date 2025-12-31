class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if len(stack) == 0 or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        else:
            if len(stack) == 0:
                return True
            return False


        