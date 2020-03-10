"""
给定两个用链表表示的整数，每个节点包含一个数位。
这些数位是反向存放的，也就是个位排在链表首部。
编写函数对这两个整数求和，并用链表形式返回结果。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = l1
        num2 = l2
        sum_node = ListNode(0)
        flag = sum_node
        # 逐位相加
        count = 0
        while num1 and num2:
            su = num1.val + num2.val
            su += count
            if su >= 10:
                num_s = su // 10  # 十位
                num_u = su % 10  # 个位
                count = num_s  # 进1

                node_u = ListNode(num_u)  # 个位

                flag.next = node_u
                flag = flag.next
            else:
                count = 0
                node_u = ListNode(su)  # 个位
                flag.next = node_u
                flag = flag.next
            num1 = num1.next
            num2 = num2.next

        if count == 0:
            if num1:
                flag.next = num1
            if num2:
                flag.next = num2
        else:
            if num1:
                sub_num = num1
                pre_sub = sub_num  # 记录末尾最后一个数字
                while sub_num:
                    su = sub_num.val + count
                    if su >= 10:
                        num_s = su // 10  # 十位
                        num_u = su % 10  # 个位
                        count = num_s  # 进1
                        sub_num.val = num_u
                    else:
                        count = 0
                        sub_num.val = su
                    sub_num,pre_sub = sub_num.next,sub_num
                if count == 1:
                    s = ListNode(count)
                    pre_sub.next = s
                flag.next = num1
            elif num2:
                sub_num = num2
                pre_sub = sub_num  # 记录末尾最后一个数字
                while sub_num:
                    su = sub_num.val + count
                    if su >= 10:
                        num_s = su // 10  # 十位
                        num_u = su % 10  # 个位
                        count = num_s  # 进1
                        sub_num.val = num_u
                    else:
                        count = 0
                        sub_num.val = su
                    sub_num,pre_sub = sub_num.next,sub_num
                if count == 1:
                    s = ListNode(count)
                    pre_sub.next = s
                flag.next = num2
            else:
                s = ListNode(count)
                flag.next = s

        return sum_node.next
