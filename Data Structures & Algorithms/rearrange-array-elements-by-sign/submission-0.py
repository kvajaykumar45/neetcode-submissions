class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = 0
        n = 1
        result = [0] * len(nums)
        for each in nums:
            if each > 0:
                result[p] = each
                p += 2
            else:
                result[n] = each
                n += 2
        return result