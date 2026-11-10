class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        if num1=='1':
            return num2
        if num2=='1':
            return num1
        num1=[ord(ch)-ord('0') for ch in reversed(num1)]#[3, 2, 1]
        num2=[ord(ch)-ord('0') for ch in reversed(num2)]

        offset=0
        carry=0
        res=[-1]*(len(num1)+len(num2))
        for a in num1:
            k=offset
            carry=0
            for b in num2:
                p=a*b+carry+(res[k] if res[k]!=-1 else 0)
                res[k]=p%10
                carry=p//10
                k+=1
            if carry>0:
                res[k]=carry
            offset+=1
        return ''.join([f'{d}' for d in reversed(res) if d!=-1])