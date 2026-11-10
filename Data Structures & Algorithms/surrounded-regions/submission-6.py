class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        #used=[[False]*len(board[0] for _ in range(len(board)))]
        #dirs=()
        def dfs(board,i,j):
            print('inside dfs1')
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or board[i][j]!='O':
                return
            board[i][j]='A'
            #print('inside dfs2')
            #print(i)
            #print(j)
            dfs(board,i-1,j)
            dfs(board,i,j-1)
            dfs(board,i+1,j)
            dfs(board,i,j+1)
        
        for i in range(len(board)):
            dfs(board,i,0)
            dfs(board,i,len(board[0])-1)
        #print(board)
        for j in range(1,len(board[0])-1):
            dfs(board,0,j)
            dfs(board,len(board)-1,j)
        #print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='A':
                    board[i][j]='O'
                    #print(i)
                    #print(j)
                    #print(board)
                elif board[i][j]=='O':
                    board[i][j]='X'
        