# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        arr = []
        narr = []
        while cur is not None:
            arr.append(cur.val)
            cur = cur.next
        # print(arr)
        for a in arr:
            if a != val:
                narr.append(a)
        # print(narr)
        cur = dummy = ListNode(-1)
        for n in narr:
            cur.next = ListNode(n)
            cur = cur.next
        cur.next = None
        # print(dummy)
        return dummy.next