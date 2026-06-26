class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        i = 0
        k = 0
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
            i += 1
        while k < n:
            nums[k] = 0
            k += 1