import sys
input = sys.stdin.readline
dict_file = {}
N = int(input())
for i in range(N) : 
    file = input().strip().split('.')[1]
    dict_file[file] = dict_file.get(file, 0) + 1

for i in sorted(dict_file) :
    print(i, dict_file[i])