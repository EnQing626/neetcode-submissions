class CountSquares:
    """
    题目要求：在X-Y平面上的点构成的数据流，实现初始化操作、添加点操作以及
    给一个点在平面中有多少种三个点的组合与其可以组成正方形，返回方案数量
    """
    # 解题思路：题目本身不难理解，三个操作主要是count操作需要设计一下
    # 给一个点，我们可以先遍历其对角线上的点，根据对角线的点就可以算出可以围成正方形的另外两个点的坐标，看是否在数据流中
    # 因为点可以重复出现(算不同点)，所以计算正方形的个数时需要把这三个点出现的次数相乘，即为方案数量
    # 可以用一个哈希表来存储数据流中加入的点，add操作，键为该点坐标，值为出现的次数
    def __init__(self):
        self.points = defaultdict(int)  # 初始化哈希表(字典)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1  # 更新该点出现的次数，注意键必须是不可变变量，所以不能直接用point(列表是可变变量)

    def count(self, point: List[int]) -> int:
        res = 0  # 返回的方案数量
        x, y = point  # 取出该点的横纵坐标
        for k, v in self.points.items():  # 遍历寻找其对角线上的点，k为点坐标，v为出现的次数
            if k[0] == x or k[1] == y:  # 与该点共线不能作为对角线点，跳过
                continue
            if abs(k[0] - x) != abs(k[1] - y):  # 长宽不等，不能围成正方形，跳过
                continue
            p0, p1 = (k[0], y), (x, k[1])  # 很容易计算出可以围成正方形的另外两个点的坐标
            res += v * self.points.get(p0, 0) * self.points.get(p1, 0)  # 方案数量为这三个点出现的次数相乘
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)