import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

def bfs(i,j):
    q = deque()
    q.append((i,j))
    while q:
        r,c = q.popleft()
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dy, c+dx
            if 0<=nr<N and 0<=nc<M and mat[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr,nc))
                visited[nr][nc] = 1

for t in range(T):
    N, M, K = map(int, input().split())
    mat = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for k in range(K):
        i, j = map(int, input().split())
        mat[i][j] = 1
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                cnt += 1
    print(cnt)