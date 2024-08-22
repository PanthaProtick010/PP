from math import log10, pow
m={1:"One ",2:"Two ",3:"Three ",4:"Four ",5:"Five ",6:"Six ",7:"Seven ",8:"Eight ",9:"Nine ",0:"Zero "}
num=int(input("Enter the number: "))
factor=int(log10(num))
temp=num
while(temp>0):
    dig=temp//int(pow(10,factor))
    temp=temp%int(pow(10,factor))
    factor-=1
    print(m[dig],end='')
print("\n")
