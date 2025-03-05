import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
a,b = map(int,input().split())
M = int(input())
relations = [[] for _ in range(N+1)]
for i in range(M):
    parent, child = map(int,input().split())
    relations[parent].append(child)
    relations[child].append(parent)
visited = [False for _ in range(N+1)]


def dfs(x, cnt):
    global flag
    visited[x] = True
    if x == b:
        flag = True
        print(cnt)
    for val in relations[x]:
        if visited[val] == False:
            dfs(val, cnt+1)

flag = False
dfs(a,0)
if flag == False:
    print(-1)