"""
字符串轮转。给定两个字符串s1和s2，
请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。
"""


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2 == '':
            return True

        l1 = list(s1)
        l2 = list(s2)
        length = len(l1)

        flag = False
        for i in range(length):
            first = l1[0]
            l1 = l1[1:]
            l1.append(first)
            if l1 == l2:
                flag = True
                break
        return flag

    def isFlipedString2(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return  False
        if len(s1)==len(s2)==0:
            return True

        ss1=s1+s1
        if s2 in ss1:
            return  True

        return False



if __name__ == '__main__':
    s = Solution()
    print(s.isFlipedString2("", ""))
