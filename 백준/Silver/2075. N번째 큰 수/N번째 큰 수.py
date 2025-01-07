import sys
import heapq
N = int(input())
min_heap = []
for i in range(N):
    l = list(map(int,input().split()))
    for num in l:
        if len(min_heap) < N:
            heapq.heappush(min_heap,num)
        else:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap,num)
print(min_heap[0])