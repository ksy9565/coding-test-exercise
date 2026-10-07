from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        # m: 세로길이, n: 가로길이
        m = len(grid)
        n = len(grid[0])
        
        # 2차원 좌표에서 상하좌우 한칸씩 이동하기 위함
        dx = (1,0,-1,0)
        dy = (0,1,0,-1)
        
        # BFS 알고리즘 실행 함수
        # start 좌표 (x,y)에서 BFS 시작
        # 섬의 크기 반환
        # 방문한 노드는 grid에서 0으로 바꾸어준다.
        # -> grid 전체를 루프 돌 때, 같은 섬을 재방문하지 않기 위함
        def bfs(start: tuple[int,int]) -> int:
            
            # 현재 섬 크기
            answer = 0
            
            # set: 순서 없음, 중복 삭제
            visited = set()
            visited.add(start)

            # deque: 양방향에서 push&pop 가능한 큐
            # appendleft, popleft <-> append, pop
            q = deque()
            q.append(start)

            while q:
                answer += 1
                current = q.popleft() # bfs는 FIFO: 큐, dfs는 LIFO: 스택
                x, y = current[0], current[1]
                grid[x][y] = 0

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    # 큐에 넣을 때 방문 체크를 해야 중복된 노드가 큐에 들어가지 않음
                    # 중복된 노드가 큐에 들어가면, 문제에 따라 시간 초과나 메모리 초과가 날 수 있음
                    if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited and grid[nx][ny] == 1:
                         q.append((nx,ny))
                         visited.add((nx,ny))
            
            return answer
        
        # max_ans: ans 중 가장 큰 값 저장
        max_ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = bfs((i,j))
                    max_ans = max(max_ans, ans)
        
        return max_ans