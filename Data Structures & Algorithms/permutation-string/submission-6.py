class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        len1=len(s1)
        len2=len(s2)
        
        Counter1=Counter(s1)
        #print(Counter1)
        left=0
        right=len1-1
        Counter2=Counter(s2[left:right])
        #print('Counter2 outside')
        #print(Counter2)
        while right<len2:
            #right+=1
            #print('right:'+str(right))
            Counter2[s2[right]]+=1
            print(Counter2)
            if Counter1==Counter2:
                return True
            else:
                Counter2[s2[left]]-=1
                if not Counter2[s2[left]]:
                    del Counter2[s2[left]]
                left+=1
                right+=1
        return False