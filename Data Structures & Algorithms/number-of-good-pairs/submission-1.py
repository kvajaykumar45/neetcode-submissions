class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for each in nums:
            d[each] = d.get(each,0)+1
        total = 0
        for each in d.values():
            if each != 1:
                total += (each*(each-1))//2
        return total