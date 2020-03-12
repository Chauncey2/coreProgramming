"""
给定一个有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。

解题思路，记录已经遍历过的节点，当读到已经遍历过的节点的时候，则返回
1.记录值
2.记录引用
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        遍历链表进哈希表，然后判断是否存在环
        :param head:
        :return:
        """
        p = head
        hash_dict = {}
        while p:
            if p in hash_dict:
                return p
            hash_dict[p], p = p, p.next

        return None

    def detectCycle2(self, head: ListNode) -> ListNode:
        """
        快慢指针（不占用额外空间）
        :param head:
        :return:
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != head:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
