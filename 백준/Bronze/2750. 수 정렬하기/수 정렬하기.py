N = int(input())
numbers = [int(input()) for i in range(N)]
numbers.sort()
# print(numbers)
# numbers = []
# for i in range(N) : 
#     number = int(input())
#     numbers.append(number)

print(*numbers, sep='\n')