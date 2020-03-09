"""
返回第k个节点
输入： 1->2->3->4->5 和 k = 2
输出： 4
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        pre = head
        las = head
        tag = 1
        # las指针先向后移动k个位置
        while tag != k and las.next:
            las = las.next
            tag += 1

        while las.next:
            pre = pre.next
            las = las.next

        return pre.val
