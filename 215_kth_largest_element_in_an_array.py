import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        q = []
        for x in nums:
            heapq.heappush(q, x)
            if len(q) > k: # 모두 push 후 중복 체크하며 pop 해도 되지만, 그냥 미리 버려도 됨
                heapq.heappop(q)

        # 파이썬 heapq는 최소 힙을 사용함. 루트가 k개 원소 중 k번째로 큰 값임.
        return q[0]