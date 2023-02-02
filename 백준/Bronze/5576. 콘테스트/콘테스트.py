# 5576.
for i in range(2) :
    print(sum(sorted([int(input()) for i in range(10)], reverse=True)[:3]), end=' ')
print()