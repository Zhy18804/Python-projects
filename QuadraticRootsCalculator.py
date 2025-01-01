import math

a = float(input("Enter first coeffcient:"))
b = float(input("Enter second coeffcient:")) 
c = float(input("Enter third coeffcient:")) 
dis = (b*b)-4*a*c
bottomNum = a * 2

if dis < 0:
    dis = dis * -1
    interceptone = str((-b + math.sqrt(dis))/bottomNum)
    intercepttwo = str((-b - math.sqrt(dis))/bottomNum)
    imagin = "i"
    print("The x-intercepts are", interceptone + imagin, "i and", intercepttwo + imagin, "i")
elif dis==0:
    intercept = -b/bottomNum
    if intercept == 0:
        print("The x-intercepts is 0")
    else:
        print("The x-intercepts is", intercept)
else:
    firstintercept = (-b + math.sqrt(dis))/bottomNum
    secondintercept = (-b - math.sqrt(dis))/bottomNum

    print("The x-intercepts are", firstintercept, "and", secondintercept)
