class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        isPal=lambda x:x==x[::-1]
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return isPal(s[left+1:right+1]) or isPal(s[left:right])
        return True