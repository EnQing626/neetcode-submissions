class Solution:
    def isHappy(self, n: int) -> bool:
        def calnum(n):
            sum_n=0
            while n:
                sum_n+=(n%10)**2
                n=n//10
            return sum_n
        used=set()
        while True:
            n=calnum(n)
            if n==1:
                return True
            if n in used:
                return False
            else:
                used.add(n)