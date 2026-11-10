class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        def lcp(str1,str2):
            length=min(len(str1),len(str2))
            index=0
            while index<length and str1[index]==str2[index]:
                index+=1
            return str1[:index]
        prefix=strs[0]
        for i in range(1,len(strs)):
            prefix=lcp(prefix,strs[i])
            if not prefix:
                break
        return prefix