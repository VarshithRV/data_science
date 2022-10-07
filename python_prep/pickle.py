# file handling using pickle
# pickle.load("datastr",file_pointer) : mode rb, wb
# pickle.dump(file_pointer)
# f = open("<filename>","mode") mode rb, wb
import pickle

fp = open("file_1.dat","wb") # open a binary file with write mode
d = {"Name": "Varshith","Rollno":"CS20B1096"}
#print(d)
pickle.dump(d,fp)

fp = open("file_1.dat","rb") # open in read mode
while True:
    try:
        d2 = pickle.load(fp)
        print(d2)
    except EOFError:
        print("done")
        break

#d2 = pickle.load(fp)


