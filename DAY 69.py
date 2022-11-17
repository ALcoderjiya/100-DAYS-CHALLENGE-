
def hcf(n1,n2):
    rem = n1 % n2
    if rem == 0:
        return n2
    res = hcf(n2 , rem)
    return res

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
res = hcf(a,b)
print("HCF of ",a," and ",b," is ",res)

'''
#to find lcm using recursion
def lcm(n1, n2):  
    if n1 > n2:
        a = n1
    else:
        a = n2
    while(True):
        if a % n1 == 0 and a % n2 == 0:
            lcm = a
            break
        a += 1
    return lcm
      
a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))  
res = lcm(a,b)     
print("LCM of ",a," and ",b," is ",res)
'''