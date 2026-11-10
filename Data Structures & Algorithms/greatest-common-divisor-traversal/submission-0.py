class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        """
            做质因数分解
            O(nlogU) 并查集还有个反阿克曼函数。
        """
        mp = defaultdict(list)
        for i,x in enumerate(nums):
            """质因数分解模版开始"""
            d = 2
            while d * d <= x:
                if x % d == 0:
                    mp[d].append(i)
                    x //= d 
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                mp[x].append(i)
            """质因数分解模版结束"""
        n = len(nums)
        """并查集模版开始"""
        fa = list(range(n))
        cnt = n
        def find(x: int) -> int:
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        """并查集模版结束"""
        for lst in mp.values():
            for a,b in pairwise(lst):
                a,b = find(a),find(b)
                if a == b: continue
                #b -> a
                fa[b] = a
                cnt -= 1
        return cnt == 1