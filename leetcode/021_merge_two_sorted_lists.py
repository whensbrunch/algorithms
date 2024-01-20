class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        curr = dummy = ListNode()
        while list1 or list2:
            if not list1:
                curr.next = list2
                list2 = list2.next
            elif not list2:
                curr.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return dummy.next