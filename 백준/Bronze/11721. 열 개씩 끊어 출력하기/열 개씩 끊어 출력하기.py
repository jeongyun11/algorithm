word = input()
length = 0

while True :

    length += 10


    if length >= len(word) :
        print(word[length -10 : len(word)])
        break
    
    print(word[length -10 : length])

    