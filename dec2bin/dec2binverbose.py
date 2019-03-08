import math
invar=(input("Expression: "))
if int(eval(invar)) != eval(invar):
 print("Expression must return integer. Breaking.")
 exit()
i=int(eval(invar))          #Input Variable (Write the number to be converted here.)
t=i                         #Temporary Variable
v=0                         #Length Variable
temp=i                      #Not in original. Used as buffer for displaying results.
                            #Finds size of input for efficiency. Allows the program to find the value quicker by avoiding wasted operations.
while t>-1:                 #Difficult to explain, but this loop subtracts 2^v from i every cycle. After finding the increment of v that causes t<0, v+1 becomes the length of the number. Since Python lists start at 0, v is used instead of v+1. This saves precious bytes. 
 v=v+1
 print("Testing length:", v)
 t=i-2**v
 print("Result:", i, "- 2 ^", v, "=", t)
 print()
print("Length:", v)
print()
a=[0]*v                     #Initializes the list using v as the length.
for x in range(v-1,-1,-1):  #Substracts 2^x from i every cycle. If y<0, position a[x] is 0, otherwise position a[x] is 1 and y is written to i.
 y=i-2**x
 print("Current Bit:", x)
 print("Result:", i, "- 2 ^", x, "=", y)
 if y<0:
  a[-x+v-1]=0
  print("Output: 0")
 else:
  a[-x+v-1]=1
  i=y
  print("Output: 1")
 print()
print("Integer:", temp)     #Prints result.
print()
print("Binary: ", end='')
for c in a:
 print(c, end='')
print()
print()
print("List: ", a)
