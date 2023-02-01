# 1526.
N = input()

if int(N) >= int('4'*(len(N))) :
    result = '7'*(len(N))
else : result = '7'*(len(N)-1)

i = len(result)-1

while int(N) < int(result) :
    if result[i] == '7' :
        result_list = list(result)
        result_list[i] = '4' 

        for j in range(i+1, len(result)) :
            result_list[j] = '7'

        result = ''
        for i in range(len(result_list)) :
            result += result_list[i]
        i = len(result)
    i -= 1        

print(result)