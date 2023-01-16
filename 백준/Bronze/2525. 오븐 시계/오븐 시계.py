hours, minutes = map(int, input().split())

minutes_add = int(input())
minutes += minutes_add

while minutes >= 60 :
    minutes -= 60
    hours += 1

if hours >= 24 :
    hours -= 24


print(hours, minutes)