class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for ch in nums:
            d[ch] = d.get(ch, 1)+1
        n = len(nums)
        print(d)
        for each in d:
            if d[each] > n//2:
                return each

        