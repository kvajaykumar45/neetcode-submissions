class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        word = strs[0]
        i = 0
        while i < len(word):
            prefix+=word[i]
            j = 1
            while j < len(strs):
                if i < len(strs[j]) and word[i] == strs[j][i]:
                    j += 1
                    continue
                else:
                    return prefix[0:i]
                
            i += 1
        return prefix