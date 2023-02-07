N = int(input())
list1 = [tuple(map(int,input().split())) for n in range(N)]
# print(list1)


for i in range(len(list1)) :
    rank = 1
    for j in range(len(list1)) :
        if i == j : continue
        if list1[i][0] < list1[j][0] and list1[i][1] < list1[j][1] :
            rank += 1
    print(rank, end=' ')
print()    
