# 10798.
words = [list(input()) for i in range(5)]
Y = 5
X = len(max(words,key=len))

for y in range(Y) :
    if len(words[y]) < X :
        for i in range(X - len(words[y])) :
            words[y].append(None)


for x in range(X) :
    for y in range(Y) :
        if words[y][x] == None :
            continue
        print(words[y][x], end='')
