import sys
import copy
from itertools import permutations
N, M, K = map(int, input().split())
v = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    v[i][1:] = list(map(int, input().split()))

lst = []
for _ in range(K):
    lst.append(tuple(map(int, input().split())))

lst_perm = permutations(lst)

def rotate(v, r, c, S):
    for s in range(1, S+1):
        # 모서리 값 저장
        top_left = v[r-s][c-s]
        top_right = v[r-s][c+s]
        bottom_right = v[r+s][c+s]
        bottom_left = v[r+s][c-s]
        
        # 좌측 세로줄 (아래로 이동)
        for i in range(r-s, r+s):
            v[i][c-s] = v[i+1][c-s]
        
        # 하단 가로줄 (왼쪽으로 이동)
        for i in range(c-s, c+s):
            v[r+s][i] = v[r+s][i+1]
        
        # 우측 세로줄 (위로 이동)
        for i in range(r+s, r-s, -1):
            v[i][c+s] = v[i-1][c+s]
        
        # 상단 가로줄 (오른쪽으로 이동)
        for i in range(c+s, c-s+1, -1):
            v[r-s][i] = v[r-s][i-1]
        
        # 모서리 값 복원
        v[r-s][c-s+1] = top_left  # 좌상단
        v[r-s+1][c+s] = top_right  # 우상단
        v[r+s][c+s-1] = bottom_right  # 우하단
        v[r+s-1][c-s] = bottom_left  # 좌하단

def row_sum(v):
    return min(sum(row[1:]) for row in v[1:])

min_result = float('inf')
for perm in lst_perm:
    original_v = copy.deepcopy(v)
    for r, c, S in perm:
        rotate(original_v, r, c, S)
    min_result = min(min_result, row_sum(original_v))

print(min_result)
