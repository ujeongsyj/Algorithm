import sys
import json
from collections import deque


T = int(input())  # 테스트 케이스 수
for turn in range(T):
    func = input()  # 수행할 함수 p
    N = int(input())  # 배열에 들어있는 수의 개수 n

    arr_input = input().strip()  # 배열 입력
    if N == 0:
        arr = deque()  # N이 0이면 빈 deque로 처리
    else:
        arr = deque(json.loads(arr_input))  # 배열을 deque로 변환
    
    reverse_flag = False  # 뒤집힌 상태를 추적하는 플래그
    error_flag = False  # 오류 발생 여부 플래그

    for s in func:
        if s == "R":
            reverse_flag = not reverse_flag  # R이 나올 때마다 뒤집힌 상태를 토글
        elif s == "D":
            if len(arr) == 0:  # 배열이 비어 있으면 에러 발생
                error_flag = True
                break
            if reverse_flag:
                arr.pop()  # 뒤집힌 상태에서는 뒤에서 삭제
            else:
                arr.popleft()  # 정상 상태에서는 앞에서 삭제

    if error_flag:
        print("error")
    else:
        if reverse_flag:
            arr.reverse()  # 마지막에 뒤집힌 상태면 한 번 뒤집기
        print(f"[{','.join(map(str, arr))}]")  # 배열을 리스트처럼 출력
