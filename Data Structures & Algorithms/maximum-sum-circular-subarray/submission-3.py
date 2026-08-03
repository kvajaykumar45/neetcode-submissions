class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        totalsum = sum(nums)
        
        maxsum = nums[0]
        currentsum = nums[0]
        i = 1
        while i < len(nums):
            if currentsum < 0:
                currentsum = 0
            currentsum += nums[i]
            maxsum = max(maxsum, currentsum)
            i += 1

        minsum = nums[0]
        currentsum = nums[0]
        i = 1
        while i < len(nums):
            currentsum += nums[i]
            currentsum = min(nums[i], currentsum)
            minsum = min(minsum, currentsum)
            i += 1
        if maxsum < 0:
            return maxsum
        return max(maxsum, totalsum-minsum)
