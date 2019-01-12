# write a line to a end of a textfile
def writeFile(file_name, line):
    try:
        g = open(file_name,'r')
    except:
<<<<<<< HEAD
        print ("ERR: file", file_name, "is not present or can't be opened")
=======
        print("ERR: file", file_name, "is not present or can't be opened")
>>>>>>> c64096163bb32d66f9306787411e02fd77897cda

    g = open(file_name, 'w+')   # + means if the file does not exist, then python will create it
    g.write(line)
    g.close()

# If you want to replace a line of a textfile
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
<<<<<<< HEAD
    #print (lines[line_num]) #line being replaced

=======
    #print(lines[line_num]) #line being replaced
 
>>>>>>> c64096163bb32d66f9306787411e02fd77897cda
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
