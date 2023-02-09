T = int(input())

for t in range(T) : 
    number = int(input())
    a, b = 1, 0

    for i in range(number) :
        a, b = b, a + b

    print(a,b)
