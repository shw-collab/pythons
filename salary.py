#To find the gross salary of an employee
base = float(input("Base salary:"))
bonus = float(input("Bonus: "))
net=base+bonus

if net<500000:
    tax_rate=0
elif net<=1000000:
    tax_rate=0.05
else:
    tax_rate=0.20

tax=net*tax_rate

if net>2500000:
    tax +=(tax*0.10)

print(f"Net: {net} | Tax: {tax} | Gross: {net-tax}")
