class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for ch in nums:
            if ch != val:
                nums[k] = ch
                k += 1
        return k