class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        result = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.insert(0, nums[left] * nums[left])
                left += 1
            else:
                result.insert(0, nums[right] * nums[right])
                right -= 1
        return result