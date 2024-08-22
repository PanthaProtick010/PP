arr=[2200,2350,2600,2130,2190]
print(f"In February, you spent {arr[1] - arr[0]} dollars more compared to January.")
totalOfQuarter=0
for i in range(3):
    totalOfQuarter+=arr[i]
print(f"Total of first quarter: {totalOfQuarter}")
if 2000 in arr:
    print("Yes, you have spent exactly 2000 dollars in a month")
else:
    print("No, you haven't spent exactly 2000 dollars in a month")
arr.append(1980)
arr[3]-=200
print(arr)