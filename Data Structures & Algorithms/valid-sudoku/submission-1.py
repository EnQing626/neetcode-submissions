class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            storage=[]
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in storage:
                    return False
                storage.append(board[i][j])
        for i in range(9):
            storage=[]
            for j in range(9):
                if board[j][i]=='.':
                    continue
                if board[j][i] in storage:
                    return False
                storage.append(board[j][i])
        for i in range(0,9,3):
            for j in range(0,9,3):
                storage=[]
                for x in range(0,3):
                    for y in range(0,3):
                        if board[i+x][j+y]=='.':
                            continue
                        if board[i+x][j+y] in storage:
                            return False
                        storage.append(board[i+x][j+y])
        return True