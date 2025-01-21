from collections import deque
import sys
N = int(input())
arr = list(list(map(int,input().strip()))for _ in range(N))
visited = [[0]*N for _ in range(N)]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    cnt = 1
    while q:
        r, c = q.popleft()
        for dy,dx in [[-1,0],[1,0],[0,-1],[0,1]]:
            nr,nc = r+dy, c+dx
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and arr[nr][nc]==1:
                q.append((nr,nc))
                cnt += 1
                visited[nr][nc] = 1
    return cnt

lst = []
total_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            total = bfs(i,j)
            total_cnt += 1
            lst.append(total)

lst.sort()
print(total_cnt)
for i in lst:
    print(i)