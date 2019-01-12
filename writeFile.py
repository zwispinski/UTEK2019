# write a line to a end of a textfile
def writeFile(file_name, line):
    try:
        g = open(file_name,'r')
    except:
        print "ERR: file", file_name, "is not present or can't be opened"

    g = open(file_name, 'w+')   # + means if the file does not exist, then python will create it
    g.write(line)
    g.close()

# If you want to replace a line of a textfile
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    print lines[line_num] #line being replaced

    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
