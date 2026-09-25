class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ref= []
        for num in nums:
            if num in ref:
                return True
            else: 
                ref.append(num)
        return False