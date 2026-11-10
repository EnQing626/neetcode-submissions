class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = collections.Counter(s1)
        left=0
        right=len(s1)-1

        N=len(s2)
        counter2=collections.Counter(s2[0:right])
        while right<N:
            counter2[s2[right]]+=1
            if counter1==counter2:
                return True
            
            counter2[s2[left]]-=1
            if counter2[s2[left]]==0:
                del counter2[s2[left]]
            left+=1
            right+=1
        return False