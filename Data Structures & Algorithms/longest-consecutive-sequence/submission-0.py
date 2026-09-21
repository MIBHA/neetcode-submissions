class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store= set(nums)
        longest= 0
        if not nums:
            return 0
        for num in store:
            if num-1 not in store:
                current_num= num
                current_len= 1

                while current_num+1 in store:
                    current_num+=1
                    current_len+=1

                longest= max(longest, current_len)
        return longest