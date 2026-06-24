class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        length = len(nums)
        leftsum = 0
        rightsum = totalsum - nums[0]
        if leftsum == rightsum:
            return 0
        for i in range(1, len(nums)):
            leftsum += nums[i-1]
            rightsum = totalsum - leftsum - nums[i]
            if leftsum == rightsum:
                return i
        return -1