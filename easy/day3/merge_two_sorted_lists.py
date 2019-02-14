# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        link = False
        if (l1 and l2):
            while(l1 or l2):
                if l1 is None:
                    temp.next = l2
                    return link
                elif l2 is None:
                    temp.next = l1
                    return link
                else:
                    if link == False:
                        if l1.val < l2.val:
                            link = ListNode(l1.val)
                            temp = link
                            l1 = l1.next
                        else:
                            link = ListNode(l2.val)
                            temp = link
                            l2 = l2.next
                    else:
                        if l1.val < l2.val:
                            temp.next = ListNode(l1.val)
                            temp = temp.next
                            l1 = l1.next
                        else:
                            print("in")
                            temp.next = ListNode(l2.val)
                            temp = temp.next
                            l2 = l2.next
            return link
        else:
            if l1:
                return l1
            elif l2:
                return l2
            else:
                return []