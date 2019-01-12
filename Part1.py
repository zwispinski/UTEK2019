import readFile
import writeFile
import item


def PrintPart1(file_name):
    lines = readFile(file_name)
    i=0
    items =[]
    for line in lines:
        if line[0] =='(':
            items[i]=item(line)
            i+=1
    items.sort()
    for x in items:
        print(x)
    
PrintPart1(part1_in)
    
