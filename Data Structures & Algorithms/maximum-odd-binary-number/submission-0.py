class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = s.count('0')
        result = ""
        result += '1'*(ones-1)
        result += '0'*zeros
        result += '1'
        return result