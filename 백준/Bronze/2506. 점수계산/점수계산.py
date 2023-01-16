
# 2506
N = int(input())
numbers = map(int, input().split())
cnt = 0
score = 0
for number in numbers : 
    if number == 1 :
        cnt += 1
    else :
        cnt = 0
        
    score += cnt
    
print(score)