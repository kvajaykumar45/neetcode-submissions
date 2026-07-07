class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {i:n for n,i in enumerate(nums1)}
        result = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in d:
                continue
            for j in range(i+1, len(nums2)):
                if  nums2[i] < nums2[j]: 
                    result[d[nums2[i]]] = nums2[j]
                    break
        return result

        