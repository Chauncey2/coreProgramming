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


