from random import randint

def line_list(line):
    return line.split("|")[1:-1]

def convertToSudoku(lines):
    sudoku=[]
    for line in lines:
        tmp=line_list(line)
        sudoku.append(tmp)
    
    refine(sudoku)
    return sudoku

def refine(unrefined):
    i=0
    while i < len(unrefined):
        while unrefined[i]==[]:
            unrefined.remove(unrefined[i])
            if i==len(unrefined): break    
        i+=1

def collectLines(filename):
    with open(filename,"r") as f:
        
        lines=f.readlines()
        len_lines=len(lines)
        count=int(lines[0])
        rndnum=randint(1,count)
        
        new_lines=[]
        k=0
        for i in range(len_lines):
            if lines[i][0]=="#": k+=1
            if k==rndnum:
                i+=1
                while lines[i][0]!="#":
                    new_lines.append(lines[i])
                    i+=1
                break
    return new_lines

def getSudokuLog(filename):
    tmp=collectLines(filename)
    sudoku=convertToSudoku(tmp)
    return sudoku


