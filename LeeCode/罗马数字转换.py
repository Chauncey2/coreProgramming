class Solution:

    def romanToInt(self, s: str) -> int:
        romaDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        num_str = s[:]
        sum_num = 0
        index = 0
        while index <= len(num_str)-1:

            if index >= len(num_str) - 1:
                roam_str = num_str[-1:]
            else:
                roam_str = num_str[index:index + 2]

            if roam_str not in romaDict.keys():
                sum_num += romaDict[roam_str[0]]
                index += 1
            else:
                sum_num += romaDict[roam_str]
                index += 2
            print('index', index)
        return sum_num


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))
