class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_table={}
        result=0
        for num in nums:
            if num not in hash_table:
                left_length = hash_table.get(num-1,0)
                right_length = hash_table.get(num+1,0)
                cur_length = left_length + right_length+1
                if cur_length > result:
                    result=cur_length
                hash_table[num]=cur_length
                hash_table[num-left_length]=cur_length
                hash_table[num+right_length]=cur_length
        return result