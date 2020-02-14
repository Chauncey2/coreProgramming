"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))  # 列表中醉倒的三个数
print(heapq.nsmallest(3, list1))  # 列表中最小的三个数
print(heapq.nlargest(2, list2, key=lambda x: x['price']))  # 价格最大的两支股票
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))  # shares 最大的两支股票

"""
迭代工具 - 排列 / 组合 / 笛卡尔积
"""
import itertools

a = itertools.permutations('ABCD')  # 排列
b = itertools.combinations('ABCDE', 3)  # 组合
c = itertools.product('ABCD', '123')  # 笛卡尔积
print("-----------------------------")
print(a)
print(b)
print(c)

for i in a: print(i)
for i in b: print(i)
for i in c: print(i)


"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))