# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        isEvenLenList = False
        slow = fast = head

        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                isEvenLenList = True
                fast = fast.next
            if fast or not isEvenLenList:
                slow = slow.next
        
        return slow
