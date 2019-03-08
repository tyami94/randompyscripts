t=i
v=0
while t>-1:
 v=v+1
 t=i-2**v
a=[0]*v
for x in range(v-1,-1,-1):
 y=i-2**x
 if y<0:
  a[-x+v-1]=0
 else:
  a[-x+v-1]=1
  i=y
