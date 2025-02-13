import sys
import  heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
INF = sys.maxsize
dist = [[] for _ in range(N+1)]


for _ in range(M):
    s,e,c = map(int,input().split())
    dist[s].append((e,c))

def Dijkstra(start):
    heap = []
    dp = [INF] * (N + 1)
    dp[start] = 0
    heapq.heappush(heap,(0, start))
    while heap:
        cost, now = heapq.heappop(heap)
        if dp[now] < cost:
            continue
        for next_node, c in dist[now]:
            next_cost = c + cost
            if next_cost < dp[next_node]:
                dp[next_node] = next_cost
                heapq.heappush(heap,(next_cost, next_node))
    for i in range(len(dp)):
        if dp[i]== INF:
            dp[i] = 0
    return dp


result = []
for i in range(1, N+1):
    dp = Dijkstra(i)
    result.append(" ".join(map(str, dp[1:])))
sys.stdout.write("\n".join(result) + "\n")
