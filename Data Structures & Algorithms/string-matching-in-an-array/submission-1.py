class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        i=0
        while i < len(words):
            j=0
            while j < len(words):
                if i!=j:
                    if words[i] in words[j]:
                        result.add(words[i])
                j += 1
            i += 1
        return list(result)
        