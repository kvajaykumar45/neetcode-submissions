class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalind(left, right):
            while left<right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isPalind(i+1, j) or isPalind(i, j-1)
            i += 1
            j -= 1
        return True
    
        

                

        