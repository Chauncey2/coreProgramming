"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。
你可以假设字符串中只包含大小写英文字母（a至z）
"""


class Solution:
    def compressString(self, S: str) -> str:
        if len(S)<=2:
            return S
        length = len(S)
        l = list()
        tag = 0
        # 切割字符串
        for i in range(0, length - 1):
            if S[i] == S[i + 1]:
                tag += 1
            elif S[i] != S[i + 1]:
                l.append(S[i - tag:i + 1])
                tag = 0
            if (i + 1) == (length - 1):
                l.append(S[i - tag + 1:])

        # 压缩字符串
        pres_str=''
        for item in l:
            s = item[0]
            num = len(item)
            s += str(num)
            pres_str+=s


        # 返回压缩后的字符串
        return S if len(pres_str)>=len(S) else pres_str


if __name__ == '__main__':
    s = Solution()
    print(s.compressString("a"))
