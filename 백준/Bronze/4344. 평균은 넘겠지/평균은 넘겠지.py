T = int(input())
for t in range(T) :
    N = map(int,input().split())
    numbers = list(N)
    numbers.pop(0)

    avg = sum(numbers) / len(numbers)

    cnt = 0
    for number in numbers :
        if number > avg :
            cnt += 1

    print('{:.3f}%'.format(round(cnt / len(numbers) * 100,3)))
