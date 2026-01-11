class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        if not S:
            return 0

        count = 0
        stack = []
        flag = 0
        for i in S:
            if i == "(":
                flag = 1
                stack.append(i)
            if i == ")":
                if flag == 1:
                    count += 2**(len(stack)-1)
                    flag = 0                
                stack.pop()
        return count
        