from ds.listnode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True
        return False
