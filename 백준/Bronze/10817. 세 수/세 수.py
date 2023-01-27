
import heapq
numbers = list(map(int, input().split()))
# max = numbers[0]
# index = 0
# for i in range(1,len(numbers)) :
#     if numbers[i -1] < numbers[i] :
#         max = numbers[i]
#         index = i
# numbers.pop(index)
# print(max(numbers))

heapq.heapify(numbers)
heapq.heappop(numbers)
print(heapq.heappop(numbers))