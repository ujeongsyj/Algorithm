N,K=map(int,input().split())
coin = set()
for i in range(N):
    coin.add(int(input()))
INF = K+1
dp = [INF]*(K+1)
dp[0]=0
for c in coin:
    for j in range(1,K+1):
        if j-c>=0:
            dp[j]=min(dp[j],dp[j-c]+1)
ans = dp[K]
if ans == INF:
    ans = -1
print(ans)