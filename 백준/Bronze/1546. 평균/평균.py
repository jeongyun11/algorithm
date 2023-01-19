

N = int(input())
numbers = list(map(int, input().split()))

number_max = max(numbers)


for i in range(len(numbers)):
    numbers[i] = numbers[i] / number_max * 100
    
print(sum(numbers)/N)