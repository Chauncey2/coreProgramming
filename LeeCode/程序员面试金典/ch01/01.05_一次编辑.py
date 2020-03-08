"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。
给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑
"""

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        length1 = len(first)
        length2 = len(second)

        if abs(length1 - length2) > 1:
            return False

        (long_str, short_str) = (first, second) if length1 > length2 else (second, first)

        count = min(length1, length2)
        for i in range(count):
            if first[i] != second[i]:
                count = i
                break
        return long_str[count + 1:] == short_str[count:] or long_str[count+1:] == short_str[count+1:]


if __name__ == '__main__':
    s = Solution()
    rel = s.oneEditAway('pale', 'pal')
    print(rel)
