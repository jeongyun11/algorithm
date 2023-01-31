# 2592.

numbers = [int(input()) for i in range(10)]
numbers_dict = {}
for number in numbers :
    numbers_dict[number] = numbers_dict.get(number,0) + 1

print(round(sum(numbers)/len(numbers)))
print(sorted(numbers_dict.items(), key = lambda x : x[1], reverse=True)[0][0])