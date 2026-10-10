class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        ### 실제로 원형 큐를 구현하기
        
        ### O(n×k)
        # q = deque(range(1, n + 1))
        # while len(q) > 1:
        #     for _ in range(k - 1):
        #         q.append(q.popleft())
        #     q.popleft()
        # return q[0]

        ### O(n)
        first = 0
        for i in range(2, n + 1):
            first = (first + k) % i
        
        return first + 1