class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for each in nums:
            xor = xor ^ each
        diff = xor & -xor;
        a = 0;
        b = 0;
        for each in nums:
            if each & diff == 0:
                a = a ^ each
            else:
                b = b ^ each
        return [a,b]

        