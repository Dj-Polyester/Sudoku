from functools import reduce
from random import randint

def solution(sudoku):
    #possibilities
    row={
    "1":["1","2","3","4","5","6","7","8","9"],
    "2":["1","2","3","4","5","6","7","8","9"],
    "3":["1","2","3","4","5","6","7","8","9"],
    "4":["1","2","3","4","5","6","7","8","9"],
    "5":["1","2","3","4","5","6","7","8","9"],
    "6":["1","2","3","4","5","6","7","8","9"],
    "7":["1","2","3","4","5","6","7","8","9"],
    "8":["1","2","3","4","5","6","7","8","9"],
    "9":["1","2","3","4","5","6","7","8","9"]}
    column={
    "1":["1","2","3","4","5","6","7","8","9"],
    "2":["1","2","3","4","5","6","7","8","9"],
    "3":["1","2","3","4","5","6","7","8","9"],
    "4":["1","2","3","4","5","6","7","8","9"],
    "5":["1","2","3","4","5","6","7","8","9"],
    "6":["1","2","3","4","5","6","7","8","9"],
    "7":["1","2","3","4","5","6","7","8","9"],
    "8":["1","2","3","4","5","6","7","8","9"],
    "9":["1","2","3","4","5","6","7","8","9"]}
    #big squares
    square={
    "1":["1","2","3","4","5","6","7","8","9"],
    "2":["1","2","3","4","5","6","7","8","9"],
    "3":["1","2","3","4","5","6","7","8","9"],
    "4":["1","2","3","4","5","6","7","8","9"],
    "5":["1","2","3","4","5","6","7","8","9"],
    "6":["1","2","3","4","5","6","7","8","9"],
    "7":["1","2","3","4","5","6","7","8","9"],
    "8":["1","2","3","4","5","6","7","8","9"],
    "9":["1","2","3","4","5","6","7","8","9"]}

    check=0
    counter=0
    #when all small squares not full
    while check==0:
        check=1
        for i in range(9):
            for j in range(9):
                
                squareIndex=j//3+3*(i//3)
                curr=sudoku[i][j]
                #print(type(curr))
                
                #if empty
                if curr==" ":
                    #print("{},{},{} empty".format(i,j,squareIndex))
                    check=0
                    tmp=intersect(row[str(i+1)],column[str(j+1)],square[str(squareIndex+1)])
                    if len(tmp)==1:
                        sudoku[i][j]=tmp[0]
                    
                    #not solveable
                    elif counter==100:
                        sudoku[i][j]=tmp
                    

                #if not empty
                elif curr in row[str(i+1)] and curr in column[str(j+1)] and curr in square[str(squareIndex+1)]:
                    #print("{},{},{} not".format(i,j,squareIndex))
                    row[str(i+1)].remove(curr)
                    column[str(j+1)].remove(curr)
                    square[str(squareIndex+1)].remove(curr)
                #printSudoku(sudoku,9,9)
        counter+=1

"""
def checkFull(*args):
    for arg in args:
        length=len(arg)
        for i in range(length):
            if arg[str(i+1)]!=[]: return False
    return True


def intersect2(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

def intersect(*args): 
    return reduce(intersect2,args)
"""
def printSudoku(table,m,n):
	j=0
	for i in range(n):
		print(f" {i}",end="",flush=True)
	print()
	while(j < 2*m+1):
		if j%2==0:
			for i in range(n):
				print(" -",end="",flush=True)
		else:
			for i in range(n):
				index=int((j-1)/2)
				print(f"|{table[index][i]}",end="",flush=True)
			print(f"| {index}",end="",flush=True)
		print("\n",end="",flush=True)
		j+=1
def intersect(*args): 
    return reduce(lambda lst1, lst2: [value for value in lst1 if value in lst2],args)

