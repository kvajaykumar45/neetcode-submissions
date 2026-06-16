class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = set()
        for each in nums:
            if each not in k:
                k.add(each)
            else:
                return True
        return False
    