class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_dict={}
        max_length=0
        for num in nums:
            if num not in hash_dict:
                left_length=hash_dict.get(num-1,0)
                right_length=hash_dict.get(num+1,0)
                cur_length=left_length+right_length+1
                if cur_length>max_length:
                    max_length=cur_length
                hash_dict[num]=cur_length
                hash_dict[num-left_length]=cur_length
                hash_dict[num+right_length]=cur_length
        return max_length