# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        cur = head
        arr =[]
        while cur is not None:
            arr.append(cur.val)
            cur =cur.next
        # print(arr)
        # print(arr[::-1])
        if arr == arr[::-1]:
            return True
        return False
        