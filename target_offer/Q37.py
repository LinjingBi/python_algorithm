
'''
输入两个链表，找出它们的第一个公共结点。
'''
"""
根据给的ListNode类看出，是一个单向无环链表，那么如果有一个结点重复，说明剩下的都是重复的。
那么我们考虑两个长短不一的链表，在长链表的前n（两个链表长度差）个结点里是不会出现共享节点的，
因为，一旦有共享结点，长短链表必定共享一个尾节点，那么从尾节点向前数短链表长度个节点，这段范围是
共享结点可能出现的唯一区间。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # 先遍历两个链表，长出长短链表
        len1 = self.Getlength(pHead1)
        len2 = self.Getlength(pHead2)

        long, short = (pHead1, pHead2) if len1 > len2 else (pHead2, pHead1)

        times = 0
        while times < abs(len1 - len2):
            long = long.next
            times += 1

        while long and short:
            if long is short:
                return long
            long, short = long.next, short.next

        return

    def Getlength(self, head):
        length = 0
        while head is not None:
            head = head.next
            length += 1
        return length


