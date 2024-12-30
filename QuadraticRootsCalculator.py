import math


a = input("Enter first coeffcient:")
b = input("Enter second coeffcient:")
c = input("Enter third coeffcient:")

int(a)
int(b)
int(c)

bottomNumber = a * 2
topNumber = math.sqrt((b*b)-4*a*c)
firstintercept = (-b + topNumber)/bottomNumber
secondintercept = (b - topNumber)/bottomNumber

print("The x-intercepts are", firstintercept, "and", secondintercept)
