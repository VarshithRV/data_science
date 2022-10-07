def readfile(f):
    for i in f:
        print(i)
    
def write(f):
    num = (int)(input("Enter the number of entries : "))
    i = 0
    while i < num:
        list = []
        str = input("Enter the ISSN : ")
        list.append("%s"%str)
        str = input("Enter the booktitle : ")
        list.append("%s"%str)
        #str = input("Enter the price : ")
        #list.append("%s"%str)
        #str = input("Enter the edition : ")
        #list.append("%s"%str)
        #str = input("Enter the author name : ")
        #list.append("%s"%str)
        for item in list:
            f.write("%s "%item)
        f.write("\n")
        i += 1
        
if __name__ == "__main__":
    f = open("1.txt",'w')
    write(f)
    f = open("1.txt",'r')
    readfile(f)
    
