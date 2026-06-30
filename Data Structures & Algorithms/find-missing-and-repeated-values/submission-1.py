class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        missing = list()
        repeated = list()
        n = len(grid)
        
        for row in grid:
            for each in row:
                if each in seen:
                    repeated.append(each)
                else:
                    seen.add(each)
                
        for each in range(1, n**2+1):
            if each not in seen:
                missing.append(each)
        
        return repeated + missing