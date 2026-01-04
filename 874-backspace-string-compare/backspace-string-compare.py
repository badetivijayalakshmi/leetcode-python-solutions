class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            stack = []
            for ch in string:
                if ch != "#":
                    stack.append(ch)
                elif stack:
                    stack.pop()

            return stack
        return process(s) == process(t)
        