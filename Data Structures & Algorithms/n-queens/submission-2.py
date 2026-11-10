class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==0:
            return []
        board=[['.']*n for _ in range(n)]
        res=[]
        def is_valid(board,row,col):
            #lie
            for i in range(row):
                if board[i][col]=='Q':
                    return False
            #zuoshang
            i=row-1
            j=col-1
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1
            #youshang
            i=row-1
            j=col+1
            while i>=0 and j<len(board):
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1
            return True

        def backtracking(board,row,n):
            if row==n:
                temp_res=[]
                for temp in board:
                    temp=''.join(temp)
                    temp_res.append(temp)
                res.append(temp_res)
            for col in range(n):
                if is_valid(board,row,col):
                    board[row][col]='Q'
                    backtracking(board,row+1,n)
                    board[row][col]='.'

        backtracking(board,0,n)
        return res