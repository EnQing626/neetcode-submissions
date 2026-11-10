class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_left, stack_star=[],[]
        for i in range(len(s)):
            if s[i]=='(':
                stack_left.append(i)
            elif s[i]=='*':
                stack_star.append(i)
            elif s[i]==')':
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
        while stack_left:
            if not stack_star:
                return False
            elif stack_left[-1]>stack_star[-1]:
                return False
            stack_left.pop()
            stack_star.pop()
        return True