'''
反转链表
输入一个链表，反转链表后，输出链表的所有元素
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def ReverseList(self, head):
        cur = head
        pre = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(14)
node1.next = node2
node2.next = node3
node3.next = node4


S = Solution()
p = S.ReverseList(node1)
while p:
    print(p.val)
    p = p.next