N = int(input())
v = [[0]*N for _ in range(N)]
v1 =[0]*(2*N) #i-j
v2 =[0]*(2*N) #i+j
v3 = [0]*N #j

total = 0
def dfs(i):
    global total
    if i == N:
        total += 1
        return
    for j in range(N):
        if v1[i-j] ==0 and v2[i+j]==0 and v3[j]==0:
            v1[i-j] = 1
            v2[i+j] = 1
            v3[j] = 1
            dfs(i+1)
            v1[i - j] = 0
            v2[i + j] = 0
            v3[j] = 0
dfs(0)
print(total)