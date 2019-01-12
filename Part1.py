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
    x = open("Part1Deliverable.txt","w+")
    x.close
    past=None
    num =0
    line = 1
    
    #Product Number: 1; Weight: 5.0; Qty: 1; Location: (2, 1)
    
    for y in items:
        if past==y:
            num+=1
            z="Product Number: " + y.content[2]+"; Weight: "+y.content[3]+"; Qty: "+str(num)+"; Location: ("+y.content[0]+", "+y.content[2]+")\n"
            replace_line("Part1Deliverable.txt",line-1,z)
        else:
            num = 1
            z="Product Number: " + y.content[2]+"; Weight: "+y.content[3]+"; Qty: "+str(num)+"; Location: ("+y.content[0]+", "+y.content[2]+")\n"
            writeFile("Part1Deliverable.txt",z)
            past = y
            line +=1



Part1("part1_in.txt")