"""
Amount=P(1+R/100)**T
ci=Amount-P
"""

p=float(input("Enter principal: "))
r=float(input("Enter rate: "))
t=float(input("Enter time: "))

# amount=p*(1+r/100)**t
# print(round(amount,2))

amount2=p*pow((1+r/100),t)
print(round(amount2,2))

ci=amount2-p
print("Compound Interest: ",round(ci,2))
