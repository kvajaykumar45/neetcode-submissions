class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {i:n for n,i in enumerate(nums1)}
        result = [-1] * len(nums1)
        stk = []
        for each in nums2:
            while stk and stk[-1] < each:
                result[d[stk.pop()]] = each
            if each in d:
                stk.append(each)
        return result
