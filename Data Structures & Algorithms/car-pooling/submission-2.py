class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d=[0]*1001
        for num, from_, to in trips:
            d[from_]+= num
            d[to]-= num
        return all(s<= capacity for s in accumulate(d))