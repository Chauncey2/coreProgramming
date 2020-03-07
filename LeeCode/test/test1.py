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


a = 'aabbccc'
a = set(a)
print(a)
d3 = dict()
s='aabbccc'
for x in s:
    d3[x] = s.count(x) # Return the number of non-overlapping occurrences of substring sub in
count=0
for item in d3.values():
    if item%2==1:
        count+=1
if count==1 or count==0:
    print('true')
print(list(d3.values()))
