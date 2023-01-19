# 2577
numbers = []
for i in range(3) :
    numbers.append(int(input()))

num_mul = 1
dict_count = {}

for number in numbers :
    num_mul *= number

# just int
# while num_mul >= 1 :
#     dict_count[num_mul % 10] = dict_count.get(num_mul % 10, 0) + 1
#     num_mul = num_mul // 10

# use str
for one_num in str(num_mul) :
    dict_count[int(one_num)] = dict_count.get(int(one_num),0) + 1

for i in range(10) :
    print(dict_count.get(i,0))
