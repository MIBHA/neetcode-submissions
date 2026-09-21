class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result= 0
        initiate= 0
        for num in nums: 
            if num ==1:

                initiate+=1
                result= max(result, initiate)
            else:
                initiate= 0
        return result