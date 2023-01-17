# 1110
num = int(input())
num_first = num
count = 0

while True :
    num_tenth = (num // 10) + (num % 10)
    if num_tenth >= 10 : 
        num_tenth -= 10
        
    num = num_tenth + (num % 10) * 10
    
    count += 1
    if num == num_first :
        break

print(count)
