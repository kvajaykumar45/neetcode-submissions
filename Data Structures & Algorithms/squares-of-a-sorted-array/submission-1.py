class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0]* length
        left = 0
        pos = right = length - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
        return result
