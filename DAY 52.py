#DAY 52 SEARCH AND UPDATE A DICTIONARY
def create(demp,n):
    for i in range(n):
        ename = input("Enter employee name : ")
        sal = int(input("Enter the salary : "))
        job = input("Enter job : ")
        demp[ename] = sal

def search(demp,name):
    if name in demp:
        print("Current Salary is ",demp[name])
        demp[name] += demp[name] * 25/100
        print("Salary Updated !!!")
    else:
        print("No employee found with given name : ")
demp = {}
n = int(input("How many employees are there : "))
create(demp,n)
print("Dictionary is ",demp)
name = input("Enter Employee name whose salary has to be increased : ")
search(demp,name)

print("Dictionary is ",demp)