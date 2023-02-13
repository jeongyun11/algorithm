N, k = map(int, input().split())
list1 = list(map(int,input().split()))
print(sorted(list1, reverse=True)[k-1])