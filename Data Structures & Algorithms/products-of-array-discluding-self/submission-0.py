class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        p = 1
        prefix[0] = 1
        suffix[-1] = 1
        for i in range(1,len(nums)):
            p = p*nums[i-1]
            prefix[i] = p
        p = 1
        for i in range(len(nums)-1, 0, -1):
            p = p*nums[i]
            suffix[i-1] = p
        #print(prefix, suffix)
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result

        