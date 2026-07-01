class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        i = 0
        while i < n:
            if not nums[i] <= nums[(i+1) % n]:
                count += 1
            i += 1
        return count <= 1


        