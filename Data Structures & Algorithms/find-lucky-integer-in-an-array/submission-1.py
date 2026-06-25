class Solution:
    def findLucky(self, arr: List[int]) -> int:
        f = {}
        for each in arr:
            f[each] = f.get(each, 0) + 1
        maxi = -1
        for k,v in f.items():
            if k == v:
                if maxi < k:
                    maxi = k
        return maxi
