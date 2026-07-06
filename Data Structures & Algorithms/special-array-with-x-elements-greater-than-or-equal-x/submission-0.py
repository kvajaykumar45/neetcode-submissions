class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        for x in range(1,n+1):
            count=0
            for i in nums:
                if i >= x:
                    count += 1
            if count == x:
                return x
        return -1
        