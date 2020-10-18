# Given the head of a linked list and two integers m and n.
# keep first m nodes and delete next n nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# my first attempt
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        while cur:
            count = 1
            while count < m and cur.next:
                cur = cur.next
                count +=1
            count = 0
            if not cur.next:
                return head
            while count<n and cur.next:
                cur.next = cur.next.next
                count += 1
            cur = cur.next
        return head

# another solution
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        count = 1
        while cur:
            if count < m:
                count +=1
            else:
                count2 = 0
                while count2 < n and cur.next:
                    cur.next = cur.next.next
                    count2 += 1
                count = 1
            cur = cur.next
        return head
