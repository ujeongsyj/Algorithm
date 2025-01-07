N,M = map(int,input().split())
lst = sorted(list(map(int,input().split())))
total_num=set()
num = []
def bt(index,cnt):
    if cnt == M:
        total_num.add(tuple(num))
        return
    for i in range(index,N):
        num.append(lst[i])
        bt(i+1,cnt+1)
        num.pop()

bt(0,0)
sorted_result = sorted(total_num)
for seq in sorted_result:
    print(" ".join(map(str, seq)))