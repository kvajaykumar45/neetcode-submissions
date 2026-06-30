class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        missing = list()
        nums = list()
        repeated = list()
        
        for row in grid:
            for each in row:
                nums.append(each)
        n=len(grid)
        for each in nums:
            if each not in seen:
                seen.add(each)
            else:
                repeated.append(each)
        for each in range(1, n**2+1):
            if each not in seen:
                missing.append(each)
        return repeated + missing