import sys
from collections import deque
N,M = map(int,input().split())
map = list(list(map(int,input().strip()))for _ in range(N))
visited = [[0]*M for _ in range(N)]
q = deque()
q.append((0,0,1))
visited[0][0] = 1
while q:
    r,c,cnt = q.popleft()
    if (r,c) == (N-1,M-1):
        break
    for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc = r+dy, c+dx
        if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and map[nr][nc]==1:
            q.append((nr,nc,cnt+1))
            visited[nr][nc] = 1
print(cnt)