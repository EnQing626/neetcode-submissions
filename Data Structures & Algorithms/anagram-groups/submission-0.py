class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        mp=collections.defaultdict(list)
        for st in strs:
            cnt=[0]*26
            for ch in st:
                cnt[ord(ch)-ord('a')]+=1
            mp[tuple(cnt)].append(st)
        return list(mp.values())
