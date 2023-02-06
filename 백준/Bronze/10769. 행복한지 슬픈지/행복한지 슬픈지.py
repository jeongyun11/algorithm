# 10769.
string = input()

if (':-(' not in string) and (':-)' not in string) :
    print('none')
else :
    cnt = 0 
    cnt -= string.count(':-(')
    cnt += string.count(':-)')

    # cnt = 0
    # for i in range(len(string)-2) :
    #     if string[i : i+2] == ':-' :
    #         if string[i+2] == ')' : cnt += 1
    #         if string[i+2] == '(' : cnt -= 1

    if cnt < 0 : print('sad')
    elif cnt > 0 : print('happy')
    else : print('unsure')