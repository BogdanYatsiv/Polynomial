from Polynomial import *

cont = [(23,5),(13,1),(1,2)]
cont2 = [(-20,5),(13,3),(1,2),(5,7),(-10,10)]


a = Polinom(cont,5)
b = Polinom(cont2,10)
c = Polinom()
print("Polinom a: ",a)
print("Polinom b: ",b)
print("Polinom c: ",c,end="\n\n")

print("===Call===\n")
print(a(5),"\n")
print("===Call===\n")


c = a+b
print("Now c is sum of a & b: ",c,end="\n\n")

print("Values of a: ",end="")
for x in a:
    print(x,end=" ")
print("\n")

print("First elem of a: ",a[1],"\nWe can change it on smt other, a[1] = 0, a[2] = 13")
a[1] = 0
a[2] = 13
print("Now first elem of a =",a[1],end="\n\n")



print("Values of a: ",end="")
for x in a:
    print(x,end=" ")
print("\n")

a*-3
print("We can mult Polinom on number, a * (-3):",a,"\n")

container = [(-20,5),(13,3),(1,2),(5,7),(-10,10)]

try:
    with PolynomeManager(container) as poly:
        for elem in poly:
            print(elem,end=" ")
            if elem[0] == 0:
                raise ArithmeticError("Bad number")
    print()
except ArithmeticError:
    print("I catch error!")