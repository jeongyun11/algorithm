c=0
for _ in range(int(input())):
 a=input()
 e=1
 for i in range(len(a)-1):
  if a[i+1]!=a[i] and a[i] in a[i+2:]:e=0
 if e>0:c+=1
print(c)