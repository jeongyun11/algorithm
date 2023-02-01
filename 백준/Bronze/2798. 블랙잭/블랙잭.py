N, M = map(int,input().split())
cards = list(map(int,input().split()))
sum_num = set()
list_sum = []
# for i in range(N-2) :
#     for j in range(i+1, N-1) :
#         for k in range(i+2, N) :
#             if(cards[i] +cards[j] + cards[k]) < M :
#                 list_sum.append(cards[i] +cards[j] + cards[k])
# print(sorted(list_sum,reverse=True)[0])

for i in range(N) : # 겹친다. 숫자의 중복
    for j in range(i + 1, N) :
        for k in range(j + 1, N) :
            if(cards[i] +cards[j] + cards[k]) <= M :
                list_sum.append(cards[i] +cards[j] + cards[k])
print(sorted(list_sum,reverse=True)[0])
