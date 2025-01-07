import sys
from collections import deque

N,M,V = map(int,input().split())

E = [[] for i in range(N+1)]
for _ in range(M):
    i,j = map(int, input().split())
    E[i].append(j)
    E[j].append(i)

for i in E:
    i.sort()

def dfs(v):
    visited[v] = True
    print(v,end=" ")
    for i in E[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited[v]=True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in E[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


#출력
visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)