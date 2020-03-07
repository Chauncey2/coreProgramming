"""实现一个算法，确定一个字符串 s 的所有字符是否全都不同。"""


class Solution:
    def isUnique(self, astr: str) -> bool:
        str1 = astr[:]
        str2 = astr[:]
        return len(str1) == len(set(str2))

if __name__ == '__main__':
    s=Solution()
    print(s.isUnique('abca'))