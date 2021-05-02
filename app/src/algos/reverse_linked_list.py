from ds.listnode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head

        while (head != None):
            next = head.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

# 1 2 3
# prev None
# cur = 1
# next = 2
# 1.next = None
# prev = 1
# cur = 2
# next = 3
# 2.next = 1
# prev = 2
# cur = 3
# next = None

