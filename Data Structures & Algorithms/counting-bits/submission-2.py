class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0]*(n+1)
        for i in range(n+1):
            if i%2==1:
                res[i]=res[i-1]+1
            else:
                #print(i)
                res[i]=res[int(i/2)]
        return res