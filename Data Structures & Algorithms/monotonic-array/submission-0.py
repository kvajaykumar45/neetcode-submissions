class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        i = 0
        n = len(nums)
        while i < n-1:
            if nums[i] > nums[i+1]:
                inc = False
            elif nums[i] < nums[i+1]:
                dec = False
            i += 1
        return inc or dec
