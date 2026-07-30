class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            possible = i + nums[i]
            farthest = max(farthest, possible)
        return True
        