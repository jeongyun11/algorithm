numbers = list(map(int,input().split()))
while True :
    for i in range(len(numbers) - 1) :
        if numbers[i] > numbers[i + 1] :
            temp = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = temp
            print(*numbers)
    if numbers == sorted(numbers) :
        break
