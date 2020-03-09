"""
给定一幅由N × N矩阵表示的图像，其中每个像素的大小为4字节，编写一种方法，将图像旋转90度。
不占用额外内存空间能否做到？(原地旋转，在原矩阵中操作)

数学知识：线性代数中的旋转矩阵
"""


class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        # 沿着主对角线交换
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(N):
            matrix[i] = matrix[i][::-1]
