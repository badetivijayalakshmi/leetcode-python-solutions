class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op.lstrip('-').isdigit():
                stack.append(int(op))
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1]*2)
            elif op == "+":
                stack.append(stack[-1]+stack[-2])
        return sum(stack)
        