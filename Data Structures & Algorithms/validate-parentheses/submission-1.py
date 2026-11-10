class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        for c in s:
            if c=='[':
                res.append(']')
            elif c=='(':
                res.append(')')
            elif c=='{':
                res.append('}')
            elif not res or res[-1]!=c:
                return False
            else:
                res.pop()
        return True if not res else False