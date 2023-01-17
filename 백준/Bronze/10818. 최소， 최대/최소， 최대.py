N = input()
numbers = list(map(int,input().split()))
max_num = numbers[0]
min_num = numbers[0]

for i in range(1,len(numbers)) : 
    if max_num < numbers[i] :
        max_num = numbers[i]
    if min_num > numbers[i] :
        min_num = numbers[i]




# for i in range(1,len(numbers)) : 
#     if max_num < numbers[i] :
#         max_num = numbers[i]
#     elif min_num > numbers[i] :
#         min_num = numbers[i]
        
# print(min(numbers), max(numbers))

print(min_num, max_num)

