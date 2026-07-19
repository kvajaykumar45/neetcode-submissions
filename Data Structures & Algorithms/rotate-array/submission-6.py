class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        dummy = nums[(n-k):] + nums[:(n-k)]
        print(dummy)
        for i in range(len(nums)):
            nums[i] = dummy[i]
    