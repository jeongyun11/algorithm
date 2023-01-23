T = int(input())
cnt = 0
for t in range(1, T + 1) : 
    word = input()
    is_Gw = True
    if len(word) <= 2 :
        cnt += 1
    else : 
        for i in range(len(word)) :
            if i > 1 :
                if word[i] != chr_bf and word[:i+1].count(word[i]) > 1 :
                    is_Gw = False
                    break
            chr_bf = word[i]

        if is_Gw == True :
            cnt += 1

print(cnt)