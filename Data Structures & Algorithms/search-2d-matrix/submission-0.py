class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        n = rows*cols
        a = []
        for i in range(rows):
            for j in range(cols):
                a.append(matrix[i][j])
        low = 0 
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if a[mid] == target:
                return True
            elif a[mid] < target:
                low = mid + 1
            elif a[mid] > target:
                high = mid - 1
        return False
        