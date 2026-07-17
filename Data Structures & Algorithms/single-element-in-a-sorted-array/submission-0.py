class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = 0
        for each in nums:
            result = result ^ each
        return result
        