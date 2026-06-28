from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for each in strs:
            word = ''.join(sorted(each))
            groups[word].append(each)
        
        return list(groups.values())


        