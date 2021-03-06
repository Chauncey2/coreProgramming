"""
给定两个（单向）链表，判定它们是否相交并返回交点。
请注意相交的定义基于节点的引用，而不是基于节点的值。
换句话说，如果一个链表的第k个节点与另一个链表的第j个节点是同一节点（引用完全相同），则这两个链表相交。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hash_dict = {}
        while headA:
            hash_dict[headA], headA = headA, headA.next
        while headB:
            if headB in hash_dict:
                return headB

            headB = headB.next
        return None
