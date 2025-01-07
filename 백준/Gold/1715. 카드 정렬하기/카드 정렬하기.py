import heapq
N = int(input())
card = []
for i in range(N):
    heapq.heappush(card,int(input()))
total = 0
while len(card)!=1:
    one = heapq.heappop(card)
    two = heapq.heappop(card)
    sum = one+two
    total += sum
    heapq.heappush(card,sum)
print(total)