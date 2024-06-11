import sys
input = sys.stdin.readline

N = int(input())

cards = [i for i in range(1, N+1)]

i = 0
while i < len(cards) - 2:
    i += 2
    cards.append(cards[i-1])

if N == 1:
    print(1)
else :
    print(cards[i+1])