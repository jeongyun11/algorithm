# 2576
numbers = [int(input()) for i in range(7)]
nums_odd = []

for i in range(7) :
    if numbers[i] % 2 == 1 :
        nums_odd.append(numbers[i])
# print('nums_odd =', nums_odd) # test 
if nums_odd :
    print(sum(nums_odd))
    print(min(nums_odd))
else :
    print(-1)