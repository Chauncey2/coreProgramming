# d = {"a": 1}
# print(d.get('a'))
# print('a' not in d.keys())
#
# l=[1,2,3]
# print(l[2:3])
# print(l[-1:])

# s='sdsdsdsd  a   '
# s=s.strip()
# print(list(s))
# import itertools
#
#
# def permutation(s: list, i: int) -> str:
#     if i == len(s):
#         s = ''.join(s)
#         return s
#     else:
#         for j in range(i, len(s)):
#             s[j], s[i] = s[i], s[j]
#             permutation(s, i + 1)
#             s[j], s[i] = s[i], s[j]
#
#
# a = itertools.permutations('tactcoa',7)
# for item in a:
#     print(''.join(item))


# 输入："aabcccccaaa"
# 输出："a2b1c5a3"

# a = "abbccd"
#
# length = len(a)
# l=list()
# tag = 0
# for i in range(0, length - 1):
#     if a[i] == a[i + 1]:
#         tag += 1
#     elif a[i] != a[i + 1]:
#         l.append(a[i - tag:i + 1])
#         tag = 0
#     if (i + 1) == (length - 1):
#         l.append(a[i - tag + 1:])
#
# print(l)

# matrix = [
#     [9, 6, 3],
#     [8, 5, 2],
#     [7, 4, 1]
# ]
#
# matrix2 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# N = len(matrix2)
# # 沿着主对角线交换
# for i in range(N):
#     for j in range(i):
#         matrix2[i][j], matrix2[j][i] = matrix2[j][i], matrix2[i][j]
#
# for i in range(N):
#     matrix2[i]=matrix2[i][::-1]
#
# print(matrix2)

# matrix=[[]
# ]
#
# coordinates = []
# for i, item in enumerate(matrix):
#     for j, enum in enumerate(item):
#         if enum == 0:
#             coordinates.append((i, j))
# print(coordinates)
#
# col_len=len(matrix[0])
# raw_len=len(matrix)
# print(raw_len)
# for cord in coordinates:
#     print(cord)
#     # 将行清零
#     for j in range(col_len):
#         matrix[cord[0]][j]=0
#     # 将列清零
#     for i in range(raw_len):
#         matrix[i][cord[1]]=0

# import queue
#
# a=queue.Queue()
# b=queue.Queue()
# a.put(1)
# b.put(1)
# print(a==b)
# print(str(a))

s1 = "waterbottle"
s2 = "erbottlewat"

print(s1[1:])
l1=list(s1)
l2=list(s2)
first=l1.pop(0)
l1.append(first)
print(l1)