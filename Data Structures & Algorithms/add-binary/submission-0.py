class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=''
        i=len(a)-1
        j=len(b)-1
        carry=0
        while i>=0 or j>=0 or carry!=0:
            if i>=0:
                num1=int(a[i])
            else:
                num1=0
            if j>=0:
                num2=int(b[j])
            else:
                num2=0
                
            sum_=num1+num2+carry
            if sum_>=2:
                carry=1
            else:
                carry=0
            if sum_>=2:
                sum_-=2
            else:
                sum_=sum_
            res+=str(sum_)
            i-=1
            j-=1
        return res[::-1]