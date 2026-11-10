class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=set()
        col=set()
        M=len(matrix)
        N=len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in range(M):
            for j in range(N):
                if i in row or j in col:
                    matrix[i][j]=0
        #return matrix