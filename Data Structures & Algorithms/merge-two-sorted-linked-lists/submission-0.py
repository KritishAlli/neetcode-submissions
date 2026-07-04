# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        cur_nodel = dummy

        while (list1 and list2):
            if (list1.val <= list2.val):
                cur_nodel.next = list1
                list1 = list1.next
                cur_nodel = cur_nodel.next
            else:
                cur_nodel.next = list2
                list2 = list2.next
                cur_nodel = cur_nodel.next
        if list1:
            cur_nodel.next = list1
        elif list2:
            cur_nodel.next = list2
        return dummy.next