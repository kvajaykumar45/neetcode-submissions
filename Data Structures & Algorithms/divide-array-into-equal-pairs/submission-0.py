class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n%2 != 0:
            return False
        nums.sort()
        i = 0
        while i < n-1:
            if nums[i] != nums[i+1]:
                return False
            i += 2
        return True

        