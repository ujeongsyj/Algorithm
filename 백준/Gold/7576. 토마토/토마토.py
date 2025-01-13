import sys
from collections import deque
M,N = map(int,input().split())
mat = [[0]*M for _ in range(N)]
mat = list(list(map(int,input().split())) for _ in range(N))
q = deque()
visited = [[0]*M for _ in range(N)]
unable = 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            q.append((i,j,0))
            visited[i][j] = 1
        elif mat[i][j] == -1:
            unable += 1
if len(q) == M*N-unable:
    print(0)
else:
    cnt = 0
    while q:
        r,c,turn = q.popleft()
        cnt += 1
        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dy, c+dx
            if 0<=nr<N and 0<=nc<M and mat[nr][nc] == 0 and visited[nr][nc] == 0:
                q.append((nr,nc,turn+1))
                visited[nr][nc] = 1
    if cnt == N*M-unable:
        print(turn)
    else:
        print(-1)