for i in range(9) : 
    number = int(input())
    if i == 0 :
        max_num = number
        index = 0
    elif max_num < number :
        max_num = number
        index = i
        
print(max_num)
print(index + 1)

