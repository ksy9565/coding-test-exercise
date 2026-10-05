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
예제 2를 참고하여 설명
[[16, 57, 98, 11, 52],
 [49, 61, 71, 31, 39],
 [51, 41, 54, 88, 93],
 [71, 21, 31, 41, 20],
 [48, 34, 22, 50, 44]]
답: 21->31->41->50의 10.

dp 테이블 정의: 각 좌표에서 시작하는 길이 l인 등산로의 최대 높이 차이가 최소인 값
이때 등산 경로 자체를 구하는 것이 아니라, 값만 구하면 됨.

길이 2인 등산로
사용된 dp: 0으로 초기화되어있음.
길이 2 new_dp 결과
[[ 33,  4, INF,  20, INF],
 [  2, 10,  27,   8,  13],
 [ 20, 10,  17,   5, INF],
 [INF, 10,  10,   9,  21],
 [ 23, 14,   9, INF,  6]]

길이 3인 등산로
사용된 dp: 길이 2인 등산로 new_dp의 결과
길이 3 new_dp 결과
[[ 33, 10, INF,  20, INF],
 [ 12, 27, INF,  13, INF],
 [INF, 17,  27, INF, INF],
 [INF, 10,  10,  47,  21],
 [INF, 23,  10, INF, INF]]

길이 4인 등산로
사용된 dp: 길이3인 등산로 new_dp의 결과
길이 4 new_dp 결과
[[ 33,  27, INF,  20, INF],
 [ 27, INF, INF, INF, INF],
 [INF,  27, INF, INF, INF],
 [INF,  10,  27, INF,  47],
 [INF, INF,  10, INF, INF]]
답 : 10

해설:
등산로 길이 2~K인 동안의 dp 테이블을 계산할 것임.

new_dp는 dp로 넘겨준 후 INF로 초기화
(길이별 dp 테이블을 모두 들고 있으면 메모리 초과하므로 직전 테이블만 저장)

각 칸에서 최소가 되는 다음 칸만 골라 계산 후 저장할 것이니까,
길이가 K가 될 때까지 반복하면 최소인 값을 구하는 것이나 마찬가지.
다음 칸의 결과를 매 라운드마다 한칸씩 땡겨온다고 생각하면 좋음

로직:
for문 안에서 칸 하나하나를 돌며 상하좌우 4칸과 비교함.
if 현재 칸보다 높은 칸에 대해서:
    diff = 높이 차이;
    max(diff, dp[ni][nj]) => 등산로 중 최대 높이 차이
    └────┬──────────────┘
    min(max, new_dp[i][j]) => 등산로 중 최대 높이 차이의 최소(4방향 중 최소인 경로를 뜻함)

dp = new_dp를 통해 계산 결과를 dp에 저장하여 다음 계산에 사용

실제 계산 과정:
dp[0][1]에서 시작하는 길이 2 등산로는 57->61에서 4를 얻음.
길이 3 등산로에서 61->71에서 10을 얻어, 기존 높이인 4보다 크기 때문에 10을 채택.
max(diff, dp[ni][nj])가 바로 이 내용

그런데, 4방향을 모두 계산하기 때문에 경로가 2가지 이상 나올 수 있음.
예를 들어, 57->98로 가는 경우와, 57->61로 가는 경우가 있는데,
57->98을 먼저 계산해서 41을 new_dp[0][1]에 들고 있어도
나중에 57->61을 계산할 때 new_dp[0][1] = min(4, 41)에서 4가 채택되기 때문에 최소가 됨.

이제 길이 3인 등산로를 계산한다고 하자. dp[i][j] = dp[0][1]일 때,
57->98을 먼저 계산하면
new_dp = min(max(41, INF), INF) = INF 이고,
그 후 57->61을 계산하면
new_dp = min(max(4, 10), INF) = 10이므로 10이 저장된다.

이 과정을 각 칸마다 반복하므로 57이 61을 선택할 때, 61에서 계산한 최소 경로를 사용하게 되는 것이다.
따라서 다음 2~K번째칸까지의 결과가 첫 칸에 전파되는 형태를 갖추고 있다.
#################################################
### 최적화 문제 -> 선택 문제 -> 이분 탐색: 시간복잡도 O(N²log2^27)=O(27N²)

# 높은 높이부터 처리하기 위한 임시 배열 생성
temp = [(grid[i][j], i, j) for i in range(N) for j in range(N)]
temp.sort(reverse=True)

# X 이하로만 이동할 때, 길이 K 이상인 등산로가 있는가
def below(X) -> bool:
    # dp[i][j] = (i,j)에서 시작하는 최장 경로의 길이
    dp = [[0]*N for _ in range(N)]

    max_len = 0
    # v가 높은 순으로 순회해야 diff 양수일 때 dp[ni][nj]가 먼저 저장되어있음.
    for v, i, j in temp:
        length = 0
        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            if 0 <= ni < N and 0 <= nj < N:
                diff = grid[ni][nj] - grid[i][j]
                if 0 < diff <= X: # grid[ni][nj]가 더 높고 차이 X 이하
                    # 등산로의 최장 길이를 구함
                    length = max(length, dp[ni][nj])
        
        # 가장 긴 length를 저장
        dp[i][j] = length + 1

        max_len = max(max_len, dp[i][j])
        if max_len >= K:
            return True
    
    return max_len >= K # K길이 있으면 True, 없으면 False 반환

# 이분 탐색: 최소 X를 찾기.
low, high = 0, 100_000_000 # 각 칸의 높이 최대는 10^8 이므로

if not below(high):
    print(-1)
else:
    while low < high:
        mid = (low+high)//2
        if below(mid):
            high = mid; # 다음 mid를 줄임
        else:
            low = mid + 1; # 다음 mid를 늘림

    print(low)
#################################################
