# cs20b1096
# Python script for Library management
import pickle

def readfile(f):
    # for i in f:
    #     print(i)
    
    while(True):
        try:
            x = pickle.load(f)
            print(x)
        except EOFError:
            print("Done")
            break

def write(f):
    num = (int)(input("Enter the number of entries : "))
    i = 0
    while i < num:
        list = []
        str = input("Enter the ISSN : ")
        list.append("%s"%str)
        str = input("Enter the booktitle : ")
        list.append("%s"%str)
        str = input("Enter the price : ")
        list.append("%s"%str)
        str = input("Enter the edition : ")
        list.append("%s"%str)
        str = input("Enter the author name : ")
        list.append("%s"%str)
        pickle.dump(list,f)
        i += 1

def search(f):
    str = input("Enter the string to be searched : ")
    while(True):
        try: 
            x = pickle.load(f)
            if(x[1] == str):
                print(x)
        except EOFError:
            print("Search done, not present")
            break

if __name__ == "__main__":
    # open the file : 
    f = open("Library.dat",'wb')
    write(f)
    f = open("Library.dat",'rb')
    readfile(f)
    f = open("Library.dat",'rb')
    # search(f)
    f.close()
