num_str = input() # 1
if int(num_str) < 10 :
    num_str += '0'
num_copy = num_str
count = 0

while True :
    sum_one = 0
    for num_one in num_str :
        sum_one += int(num_one)

    num_str = num_str[-1] + str(sum_one)[-1] # 새로운 수 11
    count += 1

    if num_str == num_copy :
        break

print(count)
