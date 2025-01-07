import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = []
visited = [[False]*(N) for _ in range(N)]
two_color = 0
three_color = 0
for i in range(N):
    graph.append(list(input()))


def dfs(r,c):
    visited[r][c] = True
    current_color = graph[r][c]
    for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
        nr = r+dy
        nc = c+dx
        if 0<=nr<N and 0<=nc<N and visited[nr][nc] == False:
            if graph[nr][nc] == current_color:
                dfs(nr,nc)
#적록색맹 아닌사람
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            three_color += 1
#R->G로 바꾸기
for i in range(N):
    for j in range(N):
        if graph[i][j]=='R':
            graph[i][j]='G'
visited = [[False]*(N) for _ in range(N)]
#적록색맹
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            two_color += 1

print(three_color, two_color)