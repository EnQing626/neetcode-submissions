class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        sum_=len(matrix)*len(matrix[0])
        L=0
        T=0
        R=len(matrix[0])-1
        B=len(matrix)-1
        res=[]
        while sum_>=1:
            for i in range(L,R+1):
                if sum_>=1:
                    res.append(matrix[T][i])
                    sum_-=1
            T+=1
            for i in range(T,B+1):
                if sum_>=1:
                    res.append(matrix[i][R])
                    sum_-=1
            R-=1
            for i in range(R,L-1,-1):
                if sum_>=1:
                    res.append(matrix[B][i])
                    sum_-=1
            B-=1
            for i in range(B,T-1,-1):
                if sum_>=1:
                    res.append(matrix[i][L])
                    sum_-=1
            L+=1
        return res