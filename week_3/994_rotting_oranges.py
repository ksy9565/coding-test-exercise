from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dx = (1,0,-1,0)
        dy = (0,1,0,-1)

        oranges = 0 # 오렌지 개수
        rotten = deque() # 썩은 오렌지
        visited = set()
        # 썩은 오렌지를 모두 담아 BFS 시작
        # 이때, 썩은 시간이 0인 모든 오렌지가 level 0에서 시작하기 때문에
        # 각 노드가 위치한 level = 썩은 시간이며
        # 간선 가중치가 모두 동일하면서 BFS이므로 항상 최단 시간에 썩게 됨.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j,0)) # x좌표, y좌표, 썩은 시간
                    visited.add((i,j))
                    oranges += 1
                elif grid[i][j] == 1:
                    oranges += 1

        if oranges == 0:
            return 0

        # BFS를 사용해야 함.
        # BFS는 각 노드의 level을 구할 수 있음.
        ### level을 노드에 저장하는 방법
        while rotten:

            x,y,minutes = rotten.popleft()

            oranges -= 1
            if oranges == 0: # 마지막 오렌지이면
                return minutes

            minutes += 1

            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited and grid[nx][ny] == 1:
                    rotten.append((nx,ny,minutes))
                    visited.add((nx,ny))

        return -1

        ### level을 q의 정보로 구하는 방법, 공간복잡도 덜 쓰는 대신 느림
        oranges = 0
        rotten = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j)) # x좌표, y좌표, 썩은 시간
                    visited.add((i,j))
                    oranges += 1
                elif grid[i][j] == 1:
                    oranges += 1

        if oranges == 0:
            return 0

        minutes = 0
        while rotten:
            size = len(rotten)

            oranges -= size
            if oranges == 0:
                return minutes

            for _ in range(size):
                x,y = rotten.popleft()

                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    
                    if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited and grid[nx][ny] == 1:
                        rotten.append((nx,ny))
                        visited.add((nx,ny))
            minutes += 1
        
        return -1