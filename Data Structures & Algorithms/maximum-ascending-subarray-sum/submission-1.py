class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = nums[0]
        maxi = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                s += nums[i]
            else:
                if maxi < s:
                    maxi = s
                s = nums[i]
        return max(maxi, s)