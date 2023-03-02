import sys
import heapq
input = sys.stdin.readline

list1 = []
N = int(input())


for n in range(N) :
    number = int(input())
    if number : # 0이 아니라면
        heapq.heappush(list1, number)
    else : # 0이라면
        if list1 : # 있으면
            print(heapq.heappop(list1))
        else :
            print(0)