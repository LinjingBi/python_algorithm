'''
输入一个链表，输出该链表中倒数第k个结点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if k <= 0:
            return None
        first = head
        second = head
        counter = 1  # 因为是从head开始，就已经是第一个节点了，所以从1开始
        while first and counter < k:  # 如果链表大于等于k长，first会停在第k个节点，正好是时候两个指针一起前进
            first = first.next
            counter += 1
        if not first:   # 包含了head是None和链表没有k长
            return None
        while first.next:
            first = first.next
            second = second.next
        return second

    # 找链表中点
    def FindMidNode(self, head):
        if not head:
            return None
        first = second = head
        for i in range(2):
            if not first.next:
                return second
            first = first.next
        second = second.next  # 由于first已经完成了走两步，second就要走一步，然后再继续。
        while first.next:
            first = first.next.next
            if not first:
                break
            second = second.next
        return second


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(14)
node5 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


S = Solution()
print(S.FindKthToTail(node1, 2).val)
# print(S.FindMidNode(node1).val)

