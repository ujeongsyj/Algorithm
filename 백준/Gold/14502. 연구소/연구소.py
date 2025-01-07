import sys
from copy import deepcopy
from collections import deque


N, M = map(int, input().split())
arr = [[1] * (M + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1] * (M + 2)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def cal(select):
    global virus
    arr2 = deepcopy(arr)
    virus_copy = deque(virus)  # 바이러스 큐를 복사하여 사용

    for i in select:
        ci, cj = i
        arr2[ci][cj] = 1  # 벽 설치

    while virus_copy:
        r, c = virus_copy.popleft()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if arr2[nr][nc] == 0:  # 바이러스가 퍼질 수 있는 경우
                arr2[nr][nc] = 2
                virus_copy.append((nr, nc))

    safe = 0
    for i in range(N + 2):
        for j in range(M + 2):
            if arr2[i][j] == 0:
                safe += 1

    return safe


def dfs(n, cnt):
    global max_safe
    if cnt == 3:
        max_safe = max(max_safe, cal(select))
        return

    if n >= len(space):
        return

    select.append(space[n])
    dfs(n + 1, cnt + 1)
    select.pop()

    dfs(n + 1, cnt)


space = []
virus = deque()
select = []
max_safe = 0

for i in range(N + 2):
    for j in range(M + 2):
        if arr[i][j] == 0:
            space.append((i, j))
        if arr[i][j] == 2:
            virus.append((i, j))

dfs(0, 0)
print(max_safe)
