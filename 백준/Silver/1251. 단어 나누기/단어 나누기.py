word = input()
word_list = []
for i in range(1, len(word)-1) :
    for j in range(i+1, len(word)) :
        word_list.append(word[i-1::-1]+word[j-1:i-1:-1]+word[:j-1:-1])
print(sorted(word_list)[0])
