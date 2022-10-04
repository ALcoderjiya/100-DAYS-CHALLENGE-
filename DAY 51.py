#DAY 51 CREATING A DICTIONARY FOR EMPLOYEES
def create(demp,n):
    for i in range(n):
        ename = input("Enter emply=oyee name : ")
        sal = int(input("Enter the salary : "))
        job = input("Enter job : ")
        demp[ename] = [sal,job]
        #demp.update({ename:sal})

demp = {}
n = int(input("How many employees are there : "))
create(demp,n)
print("Dictionary is ",demp)