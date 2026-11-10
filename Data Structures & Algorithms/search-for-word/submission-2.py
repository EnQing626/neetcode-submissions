class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        used=[[False]*n for _ in range(m)]
        def dfs(i,j,index):
            if index==len(word):
                return True
            if i<0 or i>=m or j<0 or j>=n:
                return False
            if used[i][j] or board[i][j]!=word[index]:
                return False
            
            used[i][j]=True
            if dfs(i+1,j,index+1) or dfs(i-1,j,index+1) or dfs(i,j+1,index+1) or dfs(i,j-1,index+1):
                return True
            used[i][j]=False

        for i in range(m):
            for j in range(n):
                if not used[i][j] and board[i][j]==word[0] and dfs(i,j,0):
                    return True
        return False