"""编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。"""


class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        coordinates = []
        for i, item in enumerate(matrix):
            for j, enum in enumerate(item):
                if enum == 0:
                    coordinates.append((i, j))

        col_len = len(matrix[0])
        raw_len = len(matrix)
        for cord in coordinates:
            # 将行清零
            for j in range(col_len):
                matrix[cord[0]][j] = 0
            # 将列清零
            for i in range(raw_len):
                matrix[i][cord[1]] = 0
