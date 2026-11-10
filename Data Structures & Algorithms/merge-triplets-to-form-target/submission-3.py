class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z=target
        a,b,c=0,0,0
        for ai,bi,ci in triplets:
            if ai<=x and bi<=y and ci<=z:
                a,b,c=max(ai,a),max(bi,b),max(ci,c)
        return (a,b,c)==(x,y,z)