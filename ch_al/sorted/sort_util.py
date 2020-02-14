"""
排序算法，查找算法
"""


def select_sort(origin_items, comp=lambda x, y: x < y):
    """
    简单选择排序
    :param origin_items: 原始序列
    :param comp: 比较函数
    :return: 排序后的序列
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(origin_items, comp=lambda x, y: x < y):
    """
    高质量冒泡排序，搅拌排序
    :param origin_items: 原始序列
    :param comp: 比较函数
    :return: 有序序列
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def merge_sort(origin_items, comp=lambda x, y: x <= y):
    """
    归并排序,递归算法
    :param items:
    :param comp:
    :return:
    """
    items = origin_items[:]
    if len(items) < 2:
        return items

    mind = len(items) // 2
    left = merge_sort(items[:mind])
    right = merge_sort(items[mind:])
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """
    合并两个序列
    :param items1:
    :param items2:
    :param comp:
    :return:
    """
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items2 += items2[index2:]
    return items


def seq_search(items, key):
    """
    顺序查找
    :param items:
    :param key:
    :return:
    """
    for i in enumerate(items):
        if items[i] == key:
            return i
    return -1


def bin_search(items, key):
    """
    折半查找
    :param items: 有序序列
    :param key: 关键字值
    :return: 所在位置下标
    """
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if items[mid] < key:
            start = mid + 1
        elif items[mid] > key:
            end = mid - 1
        else:
            return items
    return -1


if __name__ == '__main__':
    print(select_sort([3, 1, 2, 45, 4, 8, 2]))
    print(enumerate([3, 1, 2, 45, 4, 8, 2]))
    for i in enumerate([3, 1, 2, 45, 4, 8, 2]):
        print(i)
