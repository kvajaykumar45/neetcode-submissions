class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        '''n = len(nums)
        if n%2 != 0:
            return False
            '''
        h = set()
        for each in nums:
            if each not in h:
                h.add(each)
            else:
                h.remove(each)
        return not h