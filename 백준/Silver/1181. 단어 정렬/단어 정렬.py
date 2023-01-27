N = int(input())
words = set(input() for i in range(N))
dict_len = {}

for word in words :
    if len(word) not in dict_len :
        dict_len[len(word)] = []
    # else :
    dict_len[len(word)].append(word)

for i in sorted(dict_len) :
    print(*sorted(dict_len[i]), sep='\n')