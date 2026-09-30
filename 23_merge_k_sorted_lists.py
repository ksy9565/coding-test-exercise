# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        q = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(q, (node.val, i, node))

        if q:
            val, i, node = heapq.heappop(q)
            start = node
            curr = start
            if node.next:
                heapq.heappush(q, (node.next.val, i, node.next))

            while q:
                val, i, node = heapq.heappop(q)
                curr.next = node
                curr = curr.next
                if node.next:
                    heapq.heappush(q, (node.next.val, i, node.next))

        else:
            return ListNode().next
        
        return start