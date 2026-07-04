class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        f = Counter(arr)
        #print(f)
        for key,value in f.items():
            if value == 1:
                k -= 1
                if k == 0:
                    return key
        return ""