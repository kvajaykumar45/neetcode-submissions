class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        while i>=0 or j>=0 or carry:
            if i>=0:
                x = int(a[i])
            else:
                x = 0
            
            if j>=0:
                y = int(b[j])
            else:
                y = 0
            
            total = x + y + carry
            result.append(str(total%2))
            carry = total//2
            i-=1
            j-=1
        return ''.join(reversed(result))
