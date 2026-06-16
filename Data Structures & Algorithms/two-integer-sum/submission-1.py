class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            d = target - nums[i]
            for j in range(i+1, n):
                if nums[j] == d:
                    return [i,j]
        
        