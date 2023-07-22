cp = int(input("ENTER THE COST PRICE : "))
if cp>100000:
    print("15%")
elif cp>50000 and cp<=100000:
    print("10%")
else:
    print("5%")