class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            s += mat[i][i]
        r = len(mat)-1
        c = 0
        while r >= 0:
            if r != c:
                s += mat[r][c]
            r -= 1
            c += 1
        return s        
        