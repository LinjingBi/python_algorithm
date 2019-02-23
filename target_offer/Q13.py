# 给定单向链表的头指针和一个节点指针，在O(1)时间内删除单向链表节点
# 考虑：
# 0.如果头节点尾节点有一个为None，则违规输入return None
# 1.如果头节点和待删除节点为同一节点，直接删除二者，此情况也包含了链表只有头节点一个节点
# 2.待删除的是尾节点，就只有遍历链表找到尾节点的前一个节点将它的next置为None，再删除尾节点
# 3.待删除的是中间节点，就把待删除节点next的val赋值给待删除节点，并且把待删除节点的next指向next.next，然后删除next。
# 4.因为只要是删除中间节点，就一定要知道pre和next，而单向链表无法在o（1）的时间内知道待删除的pre，就可利用next这个可以获得pre和next的节点做删除操作。
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None

class Solution:
    def DeleteNode(self, pListHead, pToBeDeleted):
        if pListHead is None or pToBeDeleted is None:
            return None
        if pListHead is pToBeDeleted:
            del pListHead
            del pToBeDeleted
        elif pToBeDeleted.next is None:
            start = pListHead
            while start.next != pToBeDeleted:
                start = start.next
            start.next = None
            del pToBeDeleted
        else:
            pToBeDeleted.val = pToBeDeleted.next.val
            new_next = pToBeDeleted.next.next
            del pToBeDeleted.next
            pToBeDeleted.next = new_next


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

S = Solution()
S.DeleteNode(node1, node3)
print(node3.val)
S.DeleteNode(node1, node3)
print(node3.val)
print(node2.val)
S.DeleteNode(node1, node1)
print(node1.val)
S.DeleteNode(node1, node1)
print(node1.val)