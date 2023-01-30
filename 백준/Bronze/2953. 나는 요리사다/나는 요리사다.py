score = []
for i in range(5) :
    score.append(sum(map(int, input().split())))

for i in range(5) :
    if max(score) == score[i] :
        print(i + 1, score[i])
