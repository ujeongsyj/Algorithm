import sys
from collections import deque
s,e = map(int,input().split())
MAX = 100000
q = deque()
q.append((s,0))
visited = set()
visited.add(s)
while q:
    cur, time = q.popleft()
    if cur == e:
        print(time)
        break
    for next in [cur-1, cur+1, cur*2]:
        if 0<=next<=MAX and next not in visited:
            q.append((next,time+1))
            visited.add(next)

