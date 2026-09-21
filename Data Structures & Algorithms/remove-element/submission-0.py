class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # This tracks the index where the next valid number should go
        
        for num in nums:
            if num != val:
                nums[k] = num 
                k += 1
                
        return k  
