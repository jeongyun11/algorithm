T = int(input())
cnt = T # T개의 갯수 차후에 빼줄 것
for t in range(T) :
    word = input()
    for i in range(len(word)) : #단어의 알파벳을 하나씩
        if i >= 2 :
            if (chr_bf != word[i]) and (word[:i+1].count(word[i]) > 1) : # 위치가 3(index 2)부터, 이전 알파벳과 다른데 카운트가 1 초과다?
                # print('chr_bf =',chr_bf)
                # print('word[i] =',word[i])
                # print('t =',t)
                # print('cnt =', cnt)

                cnt -= 1
                break 
        chr_bf = word[i]
print(cnt)