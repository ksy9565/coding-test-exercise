N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
#################################################
### Bottom-up 방식의 DP: 시간복잡도 O(N²K), K<=100
# dp[i][j] = (i,j)에서 시작하는 l 길이의 등산로 중 최대 높이 차이가 최소인 값
INF = 100_000_000

dp = [[0]*N for _ in range(N)]

for l in range(2, K+1):
    new_dp = [[INF]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] > grid[i][j]:
                    diff = grid[ni][nj] - grid[i][j]
                    new_dp[i][j] = min(max(diff, dp[ni][nj]), new_dp[i][j])
    
    dp = new_dp

result = min(dp[i][j] for i in range(N) for j in range(N))
print(result if result != INF else -1)
#################################################

#################################################
# ### 최적화 문제 -> 선택 문제 -> 이분 탐색: 시간복잡도 O(N²log2^27)=O(27N²)

# # 높은 높이부터 처리하기 위한 임시 배열 생성
# temp = [(grid[i][j], i, j) for i in range(N) for j in range(N)]
# temp.sort(reverse=True)

# # X 이하로만 이동할 때, 길이 K 이상인 등산로가 있는가
# def below(X) -> bool:
#     # dp[i][j] = (i,j)에서 시작하는 최장 경로의 길이
#     dp = [[0]*N for _ in range(N)]

#     max_len = 0
#     # v가 높은 순으로 순회해야 diff 양수일 때 dp[ni][nj]가 먼저 저장되어있음.
#     for v, i, j in temp:
#         length = 0
#         for d in range(4):
#             ni = i + dx[d]
#             nj = j + dy[d]
#             if 0 <= ni < N and 0 <= nj < N:
#                 diff = grid[ni][nj] - grid[i][j]
#                 if 0 < diff <= X: # grid[ni][nj]가 더 높고 차이 X 이하
#                     # 등산로의 최장 길이를 구함
#                     length = max(length, dp[ni][nj])
        
#         # 가장 긴 length를 저장
#         dp[i][j] = length + 1

#         max_len = max(max_len, dp[i][j])
#         if max_len >= K:
#             return True
    
#     return max_len >= K # K길이 있으면 True, 없으면 False 반환

# # 이분 탐색: 최소 X를 찾기.
# low, high = 0, 100_000_000 # 각 칸의 높이 최대는 10^8 이므로

# if not below(high):
#     print(-1)
# else:
#     while low < high:
#         mid = (low+high)//2
#         if below(mid):
#             high = mid; # 다음 mid를 줄임
#         else:
#             low = mid + 1; # 다음 mid를 늘림

#     print(low)
#################################################