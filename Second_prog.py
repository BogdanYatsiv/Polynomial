from Polynomial import *
import shelve

s = shelve.open("shelve_data.slv")

poly_a = Polinom(s["A"][0],s["A"][1])
print("We got poly A from shelve: ",poly_a)

poly_b = Polinom(s["B"][0],s["B"][1])
print("We got poly B from shelve: ",poly_b)

sum = poly_a + poly_b

print("We can add them poly_a + poly_b = ", sum)

s.close()
