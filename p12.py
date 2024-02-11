salary = int(input("Enter your salary:"))
tax = 0
if salary<=10000:
    tax = tax *0
elif salary<=20000:
    x = salary-10000
    tax = x*10/100
else:
    tax = 10000*10/100
    tax+= (salary-20000)*20/100
print(tax)