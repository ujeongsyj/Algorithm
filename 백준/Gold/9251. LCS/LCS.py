import sys
str1= list(input())
str2=list(input())
v = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1] == str2[j-1]:
            v[i][j] = v[i-1][j-1]+1
        else:
            v[i][j] = max(v[i-1][j],v[i][j-1])
print(v[len(str1)][len(str2)])
