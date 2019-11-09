from Polynomial import *
import shelve
import pickle

cont = [(23,5),(13,1),(1,2)]
cont2 = [(-20,5),(13,3),(1,2),(5,7),(-10,10)]

a = Polinom(cont,5)
b = Polinom(cont2,10)

polynoms = [a,b]
pickle_data = open("pickle_data.pkl", "wb")
pickle.dump(polynoms,pickle_data)
pickle_data.close()

s = shelve.open("shelve_data.slv")
s["A"] = a.values, a.len
s["B"] = b.values, b.len
s.sync()
s.close()

with open("data.txt","w") as f:
    f.write(str(a.values)+str(a.len)+"\n")
    f.write(str(b.values)+str(b.len)+"\n")