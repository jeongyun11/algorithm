
# 2480.
nums = list(map(int,input().split()))
a = nums[0]
b = nums[1]
c = nums[2]

if a == b == c :
    price = 10000 + a * 1000
elif a == b or a == c :
    price = 1000 + a * 100
elif b == c :
    price = 1000 + b * 100
else :
    price =max(nums) * 100

print(price)