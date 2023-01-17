set_x = set()
set_y = set()
list_xy = []
for i in range(3) :
    x,y = map(int,input().split())
    list_xy.append([x,y])
    set_x.add(x)
    set_y.add(y)

for x in set_x :
    for y in set_y :
        if [x, y] not in list_xy :
            print(*[x, y])
            break
