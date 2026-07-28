class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        for i in range(r):
            for j in range(i+1, r):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for each in matrix:
            each.reverse()

            