class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==0:
            return []
        board=[['.']*n for _ in range(n)]
        result=[]
        def is_valid(board,row,col):
            #board[row][col]='Q'
            #lie
            for i in range(len(board)):
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
        def traversal(board,row,n):
            if row==n:
                temp_result=[]
                for temp in board:
                    temp_str=''.join(temp)
                    temp_result.append(temp_str)
                result.append(temp_result)
            for col in range(n):
                if not is_valid(board,row,col):
                    continue
                board[row][col]='Q'
                traversal(board,row+1,n)
                board[row][col]='.'
        traversal(board,0,n)
        return result