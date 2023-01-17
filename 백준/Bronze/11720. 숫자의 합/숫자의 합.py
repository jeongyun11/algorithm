N = input()

number = int(input())
# numbers = input()
sum = 0

while number >= 1 :
    sum += (number % 10)
    number //= 10
# for one_number in number_str :
#     sum += int(one_number)
print(sum)
