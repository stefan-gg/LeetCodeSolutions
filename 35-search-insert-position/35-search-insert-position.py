class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        else:
            
            if target < nums[0]:
                return 0
                
            if target > nums[-1]:
                return len(nums)
            
            for i in range(len(nums) - 1):
                if nums[i] < target and target < nums[i + 1]:
                    return i + 1