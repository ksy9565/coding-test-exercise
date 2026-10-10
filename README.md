# 🧩 코테준비청년 스터디

주차별 알고리즘 주제를 정해 문제를 풀고, 풀이 아이디어를 공유하는 코딩 테스트 스터디입니다.

## 📅 주차별 주제

| 주차  | 주제                     | 폴더     |
| :---: | ------------------------ | -------- |
| 1주차 | DP (Dynamic Programming) | `week_1` |
| 2주차 | 자료구조                 | `week_2` |
| 3주차 | BFS / DFS                | `week_3` |

## 👥 멤버

| 멤버                                     | 폴더                          | 사용 언어 |
| ---------------------------------------- | ----------------------------- | --------- |
| [ksy9565](https://github.com/ksy9565)    | [`ksy9565/`](./ksy9565)       | Python    |
| [SoyeonKang](https://github.com/wosyh18) | [`SoyeonKang/`](./SoyeonKang) | Java      |
| [yooooon](https://github.com/y00000nj)   | [`yooooon/`](./yooooon)       | C/C++     |

## 📁 폴더 구조

```
coding-test-study/
├── README.md
├── ksy9565/
│   ├── week_1/
│   ├── week_2/
│   └── week_3/
├── SoyeonKang/
└── yooooon/
```

## ✅ 스터디 규칙

- 매주 정해진 주제의 문제를 풀고 자신의 폴더에 업로드합니다.
- 파일명은 `문제번호_문제이름.py` 형식을 권장합니다. (예: `300_longest_increasing_subsequence.py`)
- 풀이 과정과 아이디어는 코드 주석으로 남겨, 스터디 시간에 공유합니다.
- 여러 풀이를 시도했다면 함께 남겨 비교합니다.

## 📝 풀이 기록

> 문제별로 멤버의 핵심 아이디어와 시간복잡도를 정리합니다. 아직 작성하지 않은 칸은 `-`로 둡니다.

### 1주차 · DP

| 문제                                                                                                                     | 출처          |
| ------------------------------------------------------------------------------------------------------------------------ | ------------- |
| [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)                     | LeetCode      |
| [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)                   | LeetCode      |
| [673. Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | LeetCode      |
| [편안한 워크숍](https://www.codetree.ai/ko/frequent-problems/all/problems/easy-workshop/description)                     | 현대 11차 2번 |

#### 300. Longest Increasing Subsequence

| 멤버       | 핵심 아이디어                                                                                          | 시간복잡도         |
| ---------- | ------------------------------------------------------------------------------------------------------ | ------------------ |
| ksy9565    | `dp[i]` = i번째 수로 끝나는 LIS 길이 → 이후 `lower_bound`로 증가 수열을 유지하는 이분 탐색 풀이로 개선 | O(n²) → O(n log n) |
| SoyeonKang | -                                                                                                      | -                  |
| yooooon    | -                                                                                                      | -                  |

#### 516. Longest Palindromic Subsequence

| 멤버       | 핵심 아이디어                                                                                                                         | 시간복잡도 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| ksy9565    | 구간 DP. `s[l] == s[r]`이면 `dp[l+1][r-1] + 2`, 아니면 `max(dp[l+1][r], dp[l][r-1])`. Bottom-up과 Top-down(메모이제이션) 두 방식 비교 | O(n²)      |
| SoyeonKang | -                                                                                                                                     | -          |
| yooooon    | -                                                                                                                                     | -          |

#### 673. Number of Longest Increasing Subsequence

| 멤버       | 핵심 아이디어                                                       | 시간복잡도 |
| ---------- | ------------------------------------------------------------------- | ---------- |
| ksy9565    | LIS 길이 배열 `dp`와 해당 길이 수열의 개수 배열 `count`를 함께 갱신 | O(n²)      |
| SoyeonKang | -                                                                   | -          |
| yooooon    | -                                                                   | -          |

#### 편안한 워크숍

| 멤버       | 핵심 아이디어                                                                                                                                      | 시간복잡도           |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| ksy9565    | ① 길이별 DP: 직전 길이의 테이블만 들고 "최대 높이 차이의 최솟값"을 전파 ② 최적화 → 결정 문제로 바꿔 차이 X 이하로 길이 K 등산로가 있는지 이분 탐색 | O(N²K) / O(N² log H) |
| SoyeonKang | -                                                                                                                                                  | -                    |
| yooooon    | -                                                                                                                                                  | -                    |

**배운 점**

- DP는 "가장 작은 단위의 점화식"을 먼저 세우고 반복문으로 확장한다.
- Bottom-up은 dp 배열이, Top-down은 메모(`dict`)가 이전 결과를 저장한다.
- 정렬된 상태를 유지할 수 있으면 이분 탐색으로 O(n) 비교를 O(log n)으로 줄일 수 있다.
- "최솟값을 구하라"는 최적화 문제는 "X 이하로 가능한가?"라는 결정 문제 + 이분 탐색으로 바꿔 풀 수 있다.

### 2주차 · 자료구조

| 문제                                                                                                              | 출처     |
| ----------------------------------------------------------------------------------------------------------------- | -------- |
| [146. LRU Cache](https://leetcode.com/problems/lru-cache/)                                                        | LeetCode |
| [1823. Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/) | LeetCode |
| [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)            | LeetCode |
| [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)                                   | LeetCode |

#### 146. LRU Cache

| 멤버       | 핵심 아이디어                                                                                                          | 시간복잡도  |
| ---------- | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| ksy9565    | 해시맵 + 이중 연결 리스트. `OrderedDict.move_to_end` / `popitem(last=False)` 풀이와, 노드·더미 노드를 직접 구현한 풀이 | 연산당 O(1) |
| SoyeonKang | -                                                                                                                      | -           |
| yooooon    | -                                                                                                                      | -           |

#### 1823. Find the Winner of the Circular Game

| 멤버       | 핵심 아이디어                                                        | 시간복잡도   |
| ---------- | -------------------------------------------------------------------- | ------------ |
| ksy9565    | `deque` 회전 시뮬레이션 → 요세푸스 점화식 `f = (f + k) % i`로 최적화 | O(nk) → O(n) |
| SoyeonKang | -                                                                    | -            |
| yooooon    | -                                                                    | -            |

#### 215. Kth Largest Element in an Array

| 멤버       | 핵심 아이디어                                    | 시간복잡도 |
| ---------- | ------------------------------------------------ | ---------- |
| ksy9565    | 크기 k인 최소 힙을 유지하면 루트가 k번째로 큰 값 | O(n log k) |
| SoyeonKang | -                                                | -          |
| yooooon    | -                                                | -          |

#### 23. Merge k Sorted Lists

| 멤버       | 핵심 아이디어                                                             | 시간복잡도 |
| ---------- | ------------------------------------------------------------------------- | ---------- |
| ksy9565    | 각 리스트의 head를 `(val, idx, node)`로 최소 힙에 넣고 하나씩 꺼내며 연결 | O(N log k) |
| SoyeonKang | -                                                                         | -          |
| yooooon    | -                                                                         | -          |

**배운 점**

- 언어별 LRU 구현: Python `OrderedDict`, Java `LinkedHashMap(accessOrder=true)`, C++ `list + unordered_map`.
- Python `heapq`는 최소 힙이므로, "k번째로 큰 값"은 크기 k를 유지하는 최소 힙으로 구한다.
- 힙에 노드 객체를 넣을 때는 값이 같을 때를 대비해 인덱스를 함께 넣어 비교 오류를 피한다.

### 3주차 · BFS / DFS

| 문제                                                                                        | 출처         |
| ------------------------------------------------------------------------------------------- | ------------ |
| [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)                | LeetCode     |
| [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)                      | LeetCode     |
| [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164)                 | 프로그래머스 |
| [오랜 기간 보호한 동물(1)](https://school.programmers.co.kr/learn/courses/30/lessons/59044) | 프로그래머스 |

#### 695. Max Area of Island

| 멤버       | 핵심 아이디어                                                             | 시간복잡도 |
| ---------- | ------------------------------------------------------------------------- | ---------- |
| ksy9565    | BFS. 육지 칸마다 BFS로 섬 크기를 세고, 방문한 칸은 0으로 바꿔 재방문 방지 | O(mn)      |
| SoyeonKang | -                                                                         | -          |
| yooooon    | -                                                                         | -          |

#### 994. Rotting Oranges

| 멤버       | 핵심 아이디어                                                                                                                     | 시간복잡도 |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| ksy9565    | 멀티 소스 BFS. 썩은 오렌지를 모두 큐에 넣고 시작 → BFS 레벨 = 썩는 시간. 레벨을 노드에 저장하는 방식과 큐 크기로 구하는 방식 비교 | O(mn)      |
| SoyeonKang | -                                                                                                                                 | -          |
| yooooon    | -                                                                                                                                 | -          |

#### 여행경로

| 멤버       | 핵심 아이디어                                                                                                       | 시간복잡도 |
| ---------- | ------------------------------------------------------------------------------------------------------------------- | ---------- |
| ksy9565    | DFS(스택). 도착지를 역순 정렬해 `pop()` 시 사전순으로 나오게 하고, 더 갈 곳이 없으면 경로에 추가 후 마지막에 뒤집기 | O(E log E) |
| SoyeonKang | -                                                                                                                   | -          |
| yooooon    | -                                                                                                                   | -          |

#### 오랜 기간 보호한 동물(1)

| 멤버       | 핵심 아이디어                                                          | 시간복잡도 |
| ---------- | ---------------------------------------------------------------------- | ---------- |
| ksy9565    | `LEFT JOIN ... WHERE o.animal_id IS NULL` 와 `NOT IN` 서브쿼리 두 방식 | -          |
| SoyeonKang | -                                                                      | -          |
| yooooon    | -                                                                      | -          |

**배운 점**

- BFS는 큐(FIFO), DFS는 스택(LIFO).
- 방문 체크는 **큐에 넣을 때** 해야 같은 노드가 중복으로 들어가지 않는다.
- 간선 가중치가 모두 같을 때 BFS의 레벨은 곧 최단 거리(시간)다.
- 시작점이 여러 개면 모두 큐에 넣고 한 번에 BFS를 돌린다(멀티 소스 BFS).
