class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt, idx = Counter(s), 0
        bucketNum = cnt.most_common(1)[0][1] # 桶的数目等于字符串中最多的元素的数目
        buckets = [[] for _ in range(bucketNum)]
        for c, num in cnt.most_common():
            for _ in range(num):
                buckets[idx].append(c)
                idx = (idx + 1) % bucketNum # 循环在不同桶中进行填充
        return "".join(["".join(bucket) for bucket in buckets]) if list(map(len, buckets)).count(1)<= 1 else ""