import sys
from collections import deque

N = int(input())
v=[[0]*N for _ in range(N)]
shark_size = 2
for i in range(N):
    v[i][0:] = map(int,input().split())
fish=deque()
time = 0
shark_r = 0
shark_c = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]
size_up = 0

def bfs(sr, sc, r, c):
    visited = [[-1] * N for _ in range(N)]
    q = deque([(sr, sc)])
    visited[sr][sc] = 1

    while q:
        sr, sc = q.popleft()
        if (sr, sc) == (r, c):
            return sr, sc, visited[sr][sc] - 1

        for i in range(4):
            nr = sr + dy[i]
            nc = sc + dx[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                if v[nr][nc] <= shark_size:
                    visited[nr][nc] = visited[sr][sc] + 1
                    q.append((nr, nc))

    return None


def find_fish():
    sr, sc = shark_r, shark_c
    min_dist = float('inf')
    min_r, min_c = None, None

    while fish:
        r, c = fish.popleft()
        result = bfs(sr, sc, r, c)
        if result is None:
            continue
        fr, fc, dist = result
        if dist < min_dist or (dist == min_dist and (fr < min_r or (fr == min_r and fc < min_c))):
            min_dist = dist
            min_r, min_c = r, c

    if min_r is None or min_c is None:
        return None, None, None  # 경로를 찾지 못한 경우

    return min_r, min_c, min_dist



for i in range(N):
    for j in range(N):
        if v[i][j] == 9:
            shark_r = i
            shark_c = j
            v[i][j] = 0
while True:
    fish_cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                continue
            if v[i][j] < shark_size:
                fish_cnt += 1
                fish.append((i, j))

    if fish_cnt == 0:
        break

    if fish_cnt == 1:
        r, c = fish.popleft()
        result = bfs(shark_r, shark_c, r, c)
        if result is None:
            break  # 경로를 찾지 못한 경우
        fr, fc, dist = result
        v[fr][fc] = 0
        shark_r, shark_c = fr, fc
        time += dist
        size_up += 1
        if size_up == shark_size:
            shark_size += 1
            size_up = 0

    if fish_cnt > 1:
        fr, fc, dist = find_fish()
        if fr is None or fc is None or dist is None:
            break  # 경로를 찾지 못한 경우
        v[fr][fc] = 0
        shark_r, shark_c = fr, fc
        time += dist
        size_up += 1
        if size_up == shark_size:
            shark_size += 1
            size_up = 0

print(time)
