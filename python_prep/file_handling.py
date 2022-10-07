import pickle
f = open("File2.dat","wb")

d = ["Hello"," ","World"]
pickle.dump(d,f)

f = open("File2.dat","rb")
d2 = []
while True:
    try:
        d2 = pickle.load(f)
    except EOFError:
        print("done")
        break
print(d2)
f.close()

f = open("File2.dat","wb")
d = ["Hello"," ","Varshith"]
pickle.dump(d,f)

f = open("File2.dat","rb")
d2 = []
while True:
    try:
        d2 = pickle.load(f)
    except EOFError:
        print("done")
        break
print(d2)
f.close()
