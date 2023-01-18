numbers = list(map(int,input().split()))

while numbers != sorted(numbers) :
    for i in range(len(numbers) - 1) : 
        if numbers[i] > numbers [i + 1] :
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            print(*numbers)

