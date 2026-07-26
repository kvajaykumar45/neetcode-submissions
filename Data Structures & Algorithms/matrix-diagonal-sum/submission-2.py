class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            s += mat[i][i] 
            if i != n - 1 - i:
                s += mat[i][n - 1 - i]
        return s   