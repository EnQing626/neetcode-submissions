class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        counter1=Counter(s1)
        left=0
        right=len(s1)-1
        #print('left'+str(left))
        #print('right'+str(right))
        counter2=Counter(s2[0:right])
        while right<len(s2):
            counter2[s2[right]]+=1

            if counter2==counter1:
                return True
            
            counter2[s2[left]]-=1
            if counter2[s2[left]]==0:
                del counter2[s2[left]]
            
            right+=1
            left+=1
        # print('left'+str(left))
        # print('right'+str(right))
        return False