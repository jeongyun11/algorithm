croatia = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in croatia :
    if i in word :
        word = word.replace(i,'.')
print(len(word))