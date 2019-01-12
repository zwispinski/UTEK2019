from readFile import readFile
from writeFile import writeFile
from item import item
from writeFile import replace_line

def Part1(file_name):
    lines = readFile(file_name)
    i=0
    items =[]
    for line in lines:
        if line[0] =='(':
            myitem = item(line)
            items.append(myitem)
            i+=1
    items.sort()
    a=file_name.rstrip(".in")
    a=a+".out"
    past=None
    num =0
    line = 0
    
    #Product Number: 1; Weight: 5.0; Qty: 1; Location: (2, 1)
    
    for y in items:
        if past==y:
            num+=1
            z="Product Number: " + y.content[2]+"; Weight: "+y.content[3]+"; Qty: "+str(num)+"; Location: ("+y.content[0]+", "+y.content[2]+")\n"
            b=line-1
            replace_line(a,b,z)
        else:
            num = 1
            z="Product Number: " + y.content[2]+"; Weight: "+y.content[3]+"; Qty: "+str(num)+"; Location: ("+y.content[0]+", "+y.content[2]+")\n"
            writeFile(a,z)
            past = y
            line +=1



Part1("1a.in")