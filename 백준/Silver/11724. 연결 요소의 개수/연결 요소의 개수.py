import sys
input = sys.stdin.readline
from collections import deque
q = deque()
N,M = map(int,input().split())
lst = [[] for _ in range(N+1)]
for i in range(M):
    s,e = map(int,input().split())
    lst[s].append(e)
    lst[e].append(s)

visited = set()
cnt = 0

def bfs(e):
    q.append(e)
    while q:
        s = q.popleft()
        for ne in lst[s]:
            if ne not in visited:
                q.append(ne)
                visited.add(ne)


for start in range(1,N+1):
    if start not in visited:
        cnt += 1
        visited.add(start)
        bfs(start)



print(cnt)