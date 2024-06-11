import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for t in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    print(f'#{t} {ans}')