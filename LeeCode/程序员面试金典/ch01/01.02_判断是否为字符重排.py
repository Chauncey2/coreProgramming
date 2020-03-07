"""
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：
输入: s1 = "abc", s2 = "bca"
输出: true
"""


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        # 如果两个字符的长队不相同
        as1 = list(s1)
        as2 = list(s2)
        if len(as1) != len(as2):
            return False
        for i in range(len(as1)):
            flag = False  # 记录是否发匹配到结果
            for j in range(len(as1)):
                if as1[i] == as2[j]:
                    as2[j] = '.'
                    flag = True
                    break # 跳出内层循环
            if not flag:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    astr = "asvnpzurz"
    bstr = "urzsapzvn"
    rel = s.CheckPermutation(astr, bstr)  # 预期结果为True
    print(rel)
