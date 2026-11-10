class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paths=[]
        path=''
        if n==0:
            return []
        def backtracking(l_num,r_num):
            nonlocal path
            if l_num==0 and r_num==0:
                paths.append(path[:])
            if r_num<l_num:
                return
            if l_num>0:
                path+='('
                backtracking(l_num-1,r_num)
                path=path[:-1]
            if r_num>0:
                path+=')'
                backtracking(l_num,r_num-1)
                path=path[:-1]

        backtracking(n,n)
        return paths