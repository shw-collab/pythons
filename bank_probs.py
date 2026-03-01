age=int(input("Age: "))
income = float(input("Annual Income: "))
score = int(input("Credit Score: "))

if 21<=age<=60 and score >=650:
    p=float(input("Loan Amount: "))
    t=int(input("Tenure(years): "))
    r=0.10/12

    n=t*12# no. of monthly installments

    emi=(p*r*(1+r)**n) / ((1+r)**n -1)

    print(f"Eligible! Monthly EMI: {round(emi,2)}")
    print(f"Total Repayment: {round(emi*n,2)}")
else:
    print("Not Eligible.")

