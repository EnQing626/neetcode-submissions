class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts=[0]*26
        for c in tasks:
            cnts[ord(c)-ord('A')]+=1
        maxvalue=0
        tot=0
        for i in range(26):
            maxvalue=max(maxvalue,cnts[i])
        for i in range(26):
            if maxvalue==cnts[i]:
                tot+=1
        return max(len(tasks),(n+1)*(maxvalue-1)+tot)