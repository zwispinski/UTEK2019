# write a line to a end of a textfile
def writeFile(file_name, line):
    try:
        g = open(file_name,'r')
    except:
        print ("ERR: file", file_name, "is not present or can't be opened")
        print("ERR: file", file_name, "is not present or can't be opened")

    g = open(file_name, 'a')   # + means if the file does not exist, then python will create it
    g.write(line)
    g.close()

# If you want to replace a line of a textfile
def replace_line(file_name, line_num, text):
    f = open(file_name,"r+")
    d = f.readlines()
    f.seek(0)
    x=d[len(d)-1]
    for i in d:
        if i != x:
            f.write(i)
    f.truncate()
    f.write(text)
    f.close()


   
