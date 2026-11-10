class Solution:
    def simplifyPath(self, path: str) -> str:
        res=[]
        for p in path.split('/'):
            if p=='..' and res:
                res.pop()
            elif p not in '..':
                res.append(p)
        return '/'+'/'.join(res)