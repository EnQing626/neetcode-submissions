class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. 将车辆按初始位置从小到大排序，并计算每辆车单独到达终点所需的时间
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s in cars]
        
        fleets = 0
        max_time = 0  # 记录当前车队的最晚到达时间（即队头的到达时间）
        
        # 2. 从离终点最近的车开始向后遍历（倒序）
        for time in reversed(times):
            # 如果当前车的单独到达时间大于前面的最晚时间，说明它追不上前面的车队
            if time > max_time:
                fleets += 1      # 形成一个新的独立车队
                max_time = time  # 更新新车队的速度限制（最长耗时）
                
        return fleets