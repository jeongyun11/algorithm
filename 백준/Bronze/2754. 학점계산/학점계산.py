
# # 2754
score = input()
score_num = 0.0

for i in range(4) :
    if  ord(score[0]) == (65 + i) :
        score_num = 4.0 - i

        if score[1] == '+' :
            score_num += 0.3
        elif score[1] == '-' :
            score_num -= 0.3

        break

print(score_num)
        
            
