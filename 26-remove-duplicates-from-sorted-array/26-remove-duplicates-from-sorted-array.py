class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums[:] ne pravi novi niz !!
        nums[:] = sorted(set(nums))
        return len(nums)
        