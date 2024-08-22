with open("D:\\Python\\DSA\\Hash Table\\ex1&2.csv", "r") as f:
        l=[]
        next(f)
        for line in f:
            tokens=line.split(',')
            l.append(int(tokens[1]))
sum=0
for i in range(7):
      sum+=l[i]
avg=float(sum)/7
print(f"The average temperature of the first week of January is {round(avg,2)}")
max=0
for i in range(len(l)):
      if max<l[i]:
            max=l[i]
print(f"The maximum temperature of January is {max}")