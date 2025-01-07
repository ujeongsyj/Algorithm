import sys
from collections import deque

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(N)]

def cal(r, c):
    sea = 0
    for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dy, c + dx
        if 0 <= nr < N and 0 <= nc < M and v[nr][nc] == 0:
            sea += 1
    return sea

def bfs(ice):
    next_ice = deque()
    melt = [[0] * M for _ in range(N)]
    
    while ice:
        r, c = ice.popleft()
        melt[r][c] = cal(r, c)
    
    for i in range(N):
        for j in range(M):
            if v[i][j] > 0:
                v[i][j] = max(0, v[i][j] - melt[i][j])
                if v[i][j] > 0:
                    next_ice.append((i, j))
    
    return next_ice

def move(r, c, visited):
    visited[r][c] = 1
    for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dy, c + dx
        if 0 <= nr < N and 0 <= nc < M and v[nr][nc] > 0 and visited[nr][nc] == 0:
            move(nr, nc, visited)

def dfs(ice):
    mountain = 0
    visited = [[0] * M for _ in range(N)]
    for r, c in ice:
        if visited[r][c] == 0:
            move(r, c, visited)
            mountain += 1
    return mountain

year = 0
ice = deque()

for i in range(N):
    for j in range(M):
        if v[i][j] > 0:
            ice.append((i, j))

while True:
    if not ice:
        print(0)
        break

    ice = bfs(ice)
    year += 1

    if dfs(ice) >= 2:
        print(year)
        break
