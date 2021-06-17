#Non-Functional programming
p,t,r=100000,12,12
interest=p*t*r/100
print(interest)
p,t,r=200000,12,12
interest=p*t*r/100
print(interest)
p,t,r=300000,12,12
interest=p*t*r/100
print(interest)
#Functional programming
#Called Function
def findInterest(p,t,r):
    interest = p * t * r / 100
    print(interest)
#Calling Function
findInterest(500000,24,12)
findInterest(1000000,36,18)