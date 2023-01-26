from collections import deque

N = int(input())
cards_dq = deque(range(1, N+1))
cards2 = [] #추가만 된다

while True :
    cards2.append(cards_dq.popleft())
    if len(cards_dq) == 0 :
        break
    cards_dq.append(cards_dq.popleft())

print(*cards2)