# DAY 8 Equilateral/Isosceles/Scalene Traingle
a = int(input("Enter First Side : "))
b = int(input("Enter Second Side : "))
c = int(input("Enter Third Side : "))

if a == b and b == c:
    print("Triangle is Equilateral")
elif a == b or b == c or a == c:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")
