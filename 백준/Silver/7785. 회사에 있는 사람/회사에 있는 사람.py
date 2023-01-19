import sys
N = int(input())
dict_state = {}
for n in range(N) :
    name, state = sys.stdin.readline().split()

    dict_state[name] = True if state == 'enter' else False

list_state = []
for key, value in dict_state.items() :
    if value == True : 
        list_state.append(key) 
print(*sorted(list_state,reverse=True), sep='\n')