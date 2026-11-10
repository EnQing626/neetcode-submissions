class Solution:
    def isHappy(self, n: int) -> bool:
        def cal_num(val):
            sum_=0
            while val:
                sum_+=(val%10)**2
                val=val//10
            return sum_
        record=set()
        while True:
            n=cal_num(n)
            if n==1:
                return True
            if n in record:
                return False
            else:
                record.add(n)