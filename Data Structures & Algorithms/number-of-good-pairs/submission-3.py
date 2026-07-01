class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        good = 0
        for each in nums:
            good += d.get(each,0)
            d[each] = d.get(each,0)+1
        return good