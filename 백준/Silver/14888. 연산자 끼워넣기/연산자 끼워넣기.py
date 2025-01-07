import sys
n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))
min_val = sys.maxsize
max_val = -sys.maxsize

def calc(a, b, idx):
    if idx == 0:
        return a + b
    elif idx == 1:
        return a - b
    elif idx == 2:
        return a * b
    elif idx == 3:
        if a < 0:
            return -((-a) // b)
        else:
            return a // b

def dfs(idx, current_sum):
    global min_val
    global max_val
    
    # 모든 숫자를 다 사용한 경우, 최솟값과 최댓값 갱신
    if idx == n:
        min_val = min(min_val, current_sum)
        max_val = max(max_val, current_sum)
        return
    
    for i in range(len(oper)):
        if oper[i] != 0:
            oper[i] -= 1
            dfs(idx + 1, calc(current_sum, nums[idx], i))
            oper[i] += 1

# 초기 호출
dfs(1, nums[0])

print(max_val)
print(min_val)
