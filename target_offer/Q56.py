'''
一个链表中包含环，请找出该链表的环的入口结点。
'''
"""
1. 先找环链表的环长度：
    1. 设置快慢指针，当两指针相遇时，相遇的点必在环上
    2. 从相遇处出发，一直next，直到回到相遇处，可以得到环的长度
2. 两个指针从head开始，一个先走环长个节点，然后两个指针同时一个一个的前进
3. 当两指针相遇时，相遇节点就是环的入口节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead:
            # 注意判断是否是环链表，环链表是不会出现任意节点的next为None的情况的
            # 如果有None，立即返回None
            if pHead.next:
                second = pHead.next
            else:
                return None
            if second.next:
                first = second.next
            else:
                return None
            while first is not second:
                second = second.next
                for i in range(2):
                    if not first.next:
                        return None
                    first = first.next
            return self.FindLoopNode(first, pHead)
        return None

    def FindLoopNode(self, node, Head):
        # 由于这里的node都是已经遍历过的，所以不存在next为None的情况，可以放心遍历
        worker = node.next
        nums = 1
        while worker is not node:
            nums += 1
            worker = worker.next
        head = Head
        tail = Head
        for i in range(nums):
            head = head.next
        while head is not tail:
            head = head.next
            tail = tail.next
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node1
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node1

s = Solution()
print(s.EntryNodeOfLoop(node1))
