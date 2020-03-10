"""
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。
如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。
分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        list_one = None
        list_two = None
        current_1 = None
        current_2 = None

        current = head

        while current != None:
            if current.val < x:
                if not list_one:
                    list_one = ListNode(current.val)
                    current_1 = list_one
                else:
                    current_1.next = ListNode(current.val)
                    current_1 = current_1.next
            else:
                if not list_two:
                    list_two = ListNode(current.val)
                    current_2 = list_two
                else:
                    current_2.next = ListNode(current.val)
                    current_2 = current_2.next
            current = current.next
        if not current_1:
            return list_two
        current_1.next = list_two
        return list_one
