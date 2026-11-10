class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        num_map = {'a': a, 'b': b, 'c': c}
        res = ''
        while True:
            # 贪心法-动态获取当前剩余字符里面的最大与中间的使用 less, mid, most 三个字符会实时变化
            less, mid, most = sorted(num_map.keys(), key=lambda x: num_map[x])
            # print(less, mid, most)
            if (len(res) < 2 or not res[-2] == res[-1] == most) and num_map[most] > 0:
                res += most
                num_map[most] -= 1 
            elif (len(res) >= 2 and not res[-2] == res[-1] == mid) and num_map[mid] > 0:
                res += mid
                num_map[mid] -= 1
            else:
                return res