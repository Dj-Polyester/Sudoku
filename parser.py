from multi_dim_array import MultiDimArray
from selenium import webdriver

def get_sudoku(table,driver,thread_name):
    print(thread_name+" Collecting...")

    boxes=driver.find_elements_by_xpath("//input[contains(@name,'e')]")
    i=0
    j=0 
    k=0
    for box in boxes:
        if k==81: break
        value=box.get_attribute("value")
        #print(str(k)+" "+str(value))
        #if the box is empty
        if value!="":
            table.array[i][j]=value
        j+=1
        if j==9:
            i+=1
            j=0
        k+=1
    return table.array
        
def printToFile(table,m,n,filename):
	j=0
	for i in range(n):
		print(f" {i}",end="",file=filename,flush=True)
	print(file=filename)
	while(j < 2*m+1):
		if j%2==0:
			for i in range(n):
				print(" -",end="",file=filename,flush=True)
		else:
			for i in range(n):
				index=int((j-1)/2)
				print(f"|{table[index][i]}",end="",file=filename,flush=True)
			print(f"| {index}",end="",file=filename,flush=True)
		print("\n",end="",file=filename,flush=True)
		j+=1
