with open("D://Python//Files//stocks.csv","r") as f, open("D://Python//Files//stocks2.csv","w") as out:
    out.write("Company Name, PE Ratio, PB Ratio\n")
    next(f)
    for line in f:
        arr=line.split(',')
        name=arr[0]
        price=float(arr[1])
        eps=float(arr[2])
        bv=float(arr[3])
        pe=round(price/eps,2)
        pb=round(price/bv,2)
        out.write(f"{name}, {pe}, {pb}\n")