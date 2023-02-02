# # 11286
import sys
import heapq
input = sys.stdin.readline
N = int(input())
numbers = []

for n in range(N) :
    number = int(input())
    if number != 0 :
        heapq.heappush(numbers, ((number * -1) if number < 0 else number, number))
    else : # 0이면 남아있을때 없을때
        if numbers : 
            print(heapq.heappop(numbers)[1])
        else : 
                print(0)