class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for item in s:
            if item=='(':
                stack.append(')')
            elif item=='[':
                stack.append(']')
            elif item=='{':
                stack.append('}')
                #第三种情况：栈已经为空了，没有匹配的字符了，说明右括号没有找到对应的左括号
            elif not stack or stack[-1]!=item:
                return False
            else:
                stack.pop()
        #第一种情况：已经遍历完了字符串，但是栈不为空，说明有相应的左括号没有右括号来匹配，
        return True if not stack else False