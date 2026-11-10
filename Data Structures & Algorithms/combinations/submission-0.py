class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        path=[]
        def traversal(n,k,startindex):
            nonlocal path
            if len(path)==k:
                result.append(path[:])
                return
            for i in range(startindex,n+1):
                path.append(i)
                traversal(n,k,i+1)
                path.pop()
        traversal(n,k,1)
        return result