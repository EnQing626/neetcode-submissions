class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res=[]
        path=''
        n=len(digits)
        digit_to_letter={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def traversal(digits,index):
            nonlocal path
            if index==n:
                res.append(path[:])
                return
            digit=digits[index]
            letters=digit_to_letter[digit]
            for i in range(len(letters)):
                path+=letters[i]
                traversal(digits,index+1)
                path=path[:-1]
            
        traversal(digits,0)
        return res
        