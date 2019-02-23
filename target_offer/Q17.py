'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 迭代版
    def Merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        curr1 = head1
        curr2 = head2
        pre = None
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                if not pre:
                    head = curr1
                pre = curr1
                curr1 = curr1.next
            else:
                nex = curr2.next
                if pre:
                    pre.next = curr2
                else:
                    head = curr2
                pre = curr2
                curr2.next = curr1
                curr2 = nex
        if curr2:
            pre.next = curr2
        return head
    # 递归版

    def Merge2(self, head1, head2):
        # if not head1:
        #     return head2
        # if not head2:
        #     return head1
        if head1 is None or head2 is None:
            return head1 if head1 else head2
        if head1.val < head2.val:
            head = head1
            head.next = self.Merge2(head1.next, head2)
        else:
            head = head2
            head.next = self.Merge2(head1, head2.next)
        return head


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node7 = ListNode(7)
node4.next = node5
node5.next = node6
node6.next = node7

S = Solution()
node = S.Merge(node1, node4)
while node:
    print(node.val)
    node = node.next
