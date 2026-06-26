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
            if nums[i] == 0:
                zeros.append(0)
            else:
                nums[k] = nums[i]
                k += 1
            i += 1
        
        i = n-1
        j = 0
        while j < len(zeros):
            nums[i] = zeros[j]
            j += 1
            i -= 1


        