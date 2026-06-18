class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = n = len(nums)
        for i in range(n):
            x = x ^ i ^ nums[i]
        return x
        