'''
删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        if pHead:
            tail = pHead
            if pHead.next:
                head = pHead.next
            else:
                return pHead

            pre = None
            new_head = pHead
            while head:
                if head.val == tail.val:
                    temp_head = self._delete_node(pre, head, tail)
                    new_head = new_head if pre else temp_head
                    tail = temp_head
                    head = tail.next if tail else None
                else:
                    pre = tail
                    head = head.next
                    tail = tail.next
            return new_head
        return pHead

    def _delete_node(self, pre, head, tail):
        while head.next and head.next.val == tail.val:
            head = head.next
        if pre:
            pre.next = head.next
        return head.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
h = s.deleteDuplication(node1)
while h:
    if h:
        print(h.val)
        h = h.next
    else:
        print(h)
