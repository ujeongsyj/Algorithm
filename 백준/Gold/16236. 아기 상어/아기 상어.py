import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
sr,sc = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sr,sc = i,j #초기상어 위치
            arr[i][j] = 0
size = 2
def bfs(i,j):#bfs 물고기 찾기
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((sr,sc,0))
    visited[sr][sc] = 1
    while q:
        r,c, dist = q.popleft()
        if (r,c) == (i,j):
            return dist, r,c
        for dy,dx in [(-1,0),(0,-1),(0,1),(1,0)]:
            nr,nc = r+dy,c+dx
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] <= size and visited[nr][nc] == 0:
                q.append((nr,nc,dist+1))
                visited[nr][nc] = 1
    return -1,0,0

def find_fish(sr,sc):
    min_dist = float("inf")
    min_r,min_c = float("inf"), float("inf")
    for i in range(N):
        for j in range(N):
            if 0< arr[i][j]<size:
                dist,r,c = bfs(i,j)
                if 0< dist:
                    if min_dist > dist or (min_dist == dist and r<min_r) or \
                        (min_dist == dist and r==min_r and c<min_c):
                        min_dist = dist
                        min_r,min_c = r,c
    return min_dist, (min_r,min_c)

time = 0
eat_cnt = 0
while True:
    dist, loc = find_fish(sr,sc)
    if dist == float("inf"):
        print(time)
        break
    else:
        time += dist
        sr,sc = loc
        arr[sr][sc] = 0
        eat_cnt += 1
        if eat_cnt == size:
            size += 1
            eat_cnt = 0
