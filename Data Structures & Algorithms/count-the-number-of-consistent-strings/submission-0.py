class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for each in words:
            status = True
            for i in each:
                if i not in allowed:
                    status = False
            if status:
                count += 1
        return count
                



        