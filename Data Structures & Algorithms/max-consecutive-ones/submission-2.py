class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        n = len(nums)
        for each in range(0, n):
            if nums[each] == 1:
                count += 1
            else:
                if count > maxi:
                    maxi = count
                count = 0
                
        if count > maxi:
            maxi = count
        return maxi