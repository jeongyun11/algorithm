N, M = map(int,input().split())
cards = list(map(int,input().split()))
sum_num = set()
list_sum = []
for i in range(N-2) :
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            if(cards[i] +cards[j] + cards[k]) <= M :
                sum_num.add(cards[i] +cards[j] + cards[k])
print(sorted(sum_num,reverse=True)[0])