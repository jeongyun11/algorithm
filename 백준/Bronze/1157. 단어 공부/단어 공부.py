word = input().upper()
dict_chr = {}

cnt = 0

for chr_word in word :
    dict_chr[chr_word] = dict_chr.get(chr_word,0) + 1

cnt_mostchr = max(dict_chr.values())

for chr in dict_chr :
    if dict_chr[chr] == cnt_mostchr :
        cnt += 1
        result = chr

if cnt == 1 :
    print(result)
else :
    print('?')