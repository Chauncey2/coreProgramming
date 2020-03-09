"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
输入：[1, 2, 3, 3, 2, 1]
输出：[1, 2, 3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        val=[head.val]
        result = head
        while head and head.next:
            if head.next.val not in val:
                val.append(head.next.val)
                head=head.next
            else:
                head.next=head.next.next

        return result



if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 3, 3, 2, 1]
    head = ListNode(l[0])
    q = head
    for item in l[1:]:
        p = ListNode(item)
        q = p
        q = q.next
        print(head)

    print(s.removeDuplicateNodes(head))
