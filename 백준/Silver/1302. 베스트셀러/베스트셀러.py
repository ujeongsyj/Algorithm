import sys
N = int(input())
dict = {}
for i in range(N):
    book = input()
    if book in dict:
        dict[book] += 1
    else:
        dict[book] = 1
sorted_dict = sorted(dict.items(), key=lambda x: (-x[1],x[0]))
print(sorted_dict[0][0])