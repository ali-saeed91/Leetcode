# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        arr=[]
        narr=[]
        while head is not None:
            arr.append(head.val)
            head = head.next
        print(arr)
        for i in range(len(arr)):
            if arr[i] != val:
                narr.append(arr[i])
        # arr.pop(val)
        # print(narr)
        cur = dummy = ListNode(0)
        for n in narr:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
        