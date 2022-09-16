#project to find the lcm of 3 numbers
def least_common_multiple(a, b):
    if a > b:
        greater = a
    elif b > a:
        greater = b
    else :
        print("the lcm is ", a)
    while(True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater = greater + 1
    return(f"the lcm is {lcm}")
print(least_common_multiple(a = int(input("enter the first number :\n"))
,     b = int(input("enter the second number:\n"))
))


