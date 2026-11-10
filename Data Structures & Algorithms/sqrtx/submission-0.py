class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = (l+r)//2
            temp = mid**2
            if  temp < x:
                l = mid + 1
            elif temp > x:
                r = mid - 1
            elif temp == x:
                return mid
        # r一定会停在mid**2 <= x的最大那个mid的位置，因为mid**2=x的mid如果存在的话在上面
        # 就已经返回了，所以这里只需要返回r就好了
        return r