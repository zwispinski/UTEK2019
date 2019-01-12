#Run this file with the test cases in the same folder to produce the desired output files

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
    f=open(a,'r+')
    f.truncate(0)
    f.close
    past=item('(-1,-1,-1,-1)')
    num =0
    line = 0
    
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
            
Part1('1a.in')
Part1('1b.in')
Part1('1c.in')