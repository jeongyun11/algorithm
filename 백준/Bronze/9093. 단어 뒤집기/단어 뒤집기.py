T = int(input())

for t in range(T) :
    string_str = input()
    string_list = string_str.split()

    for word in string_list : 
        print(word[::-1], end=' ')
        
    print()