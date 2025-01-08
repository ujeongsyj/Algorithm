import sys
N,X = map(int,input().split())
visitor = list(map(int,input().split()))
total_lst = []
cur_sum = sum(visitor[:X])
total_lst.append(cur_sum)
for i in range(X,N):
    cur_sum += (visitor[i]-visitor[i-X])
    total_lst.append(cur_sum)
if max(total_lst) == 0:
    print('SAD')
else:
    print(max(total_lst))
    print(total_lst.count(max(total_lst)))