# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        minHeap = []
        
        for n in lists:
            while n:
                heappush(minHeap, n.val)
                n = n.next
        
        cur = dummy
        while minHeap:
            temp = ListNode(heappop(minHeap))
            cur.next = temp
            cur = cur.next
        
        cur.next = None
        return dummy.next