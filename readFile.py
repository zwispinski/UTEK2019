# Get input from a textfile
def readFile(file_name):
    try:
        f = open(file_name,'r')
    except:
        print("ERR: file"+file_name+ "is not present or can't be opened")

    f = open(file_name,'r')
    lines = f.readlines()
    f.close()
    
    return [s[:-1] for s in lines]
