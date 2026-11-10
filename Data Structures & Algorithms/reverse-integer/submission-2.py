class Solution:
    def reverse(self, x: int) -> int:
        res=0
        signal=0
        if x==0:
            return 0
        
        if x<0:
            x=-x
            signal=1
        reverse_num=[]
        while x!=0:
            reverse_num.append(x%10)
            x=x//10
        #reverse_num.append(x)
        #print(reverse_num)
        digit=len(reverse_num)-1
        for i in range(len(reverse_num)):
            res+=reverse_num[i]*10**digit
            digit-=1
        if signal==1:
            res*=-1
        
        # 结果溢出判断
        if res < -1*2**31 or res >= 2**31:
            return 0

        # 返回结果
        return res
        
        