"""
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
回文串不一定是字典当中的单词。

示例1：
输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(set(s)) == 1 or s == '':
            return True
        d = dict()
        for item in s:
            # Return the number of non-overlapping occurrences of substring sub instring S[start:end].
            d[item] = s.count(item)

        count=0
        for item in d.values():
            if item % 2 == 1:
                count += 1
        if count == 1 or count == 0:
            return True

        return False
if __name__ == '__main__':
    s = Solution()
    print(s.canPermutePalindrome(" "))
