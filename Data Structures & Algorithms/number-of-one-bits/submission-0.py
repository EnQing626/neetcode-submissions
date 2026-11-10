class Solution:
    def hammingWeight(self, n: int) -> int:
        import collections
        return collections.Counter(str(bin(n)))['1']