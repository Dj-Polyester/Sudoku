import threading
from selenium import webdriver
import parser
import time
from multi_dim_array import MultiDimArray

NUMBER_OF_THREADS=4


# Create worker threads (will die when main exits)
def create_workers(driver):
	lock=threading.Lock()
	for i in range(NUMBER_OF_THREADS):
		tmp="thread "+str(i+1)
		t = threading.Thread(target=work,args=(driver,lock),name=tmp,daemon=True)
		t.start()

def work(driver,lock):
	thread_name=threading.current_thread().name
	print(thread_name+" started.")
	num=int(thread_name[-1])
	#create empty sudoku template
	table=MultiDimArray(9,9,num)
	table_array=table.array

	#get the website to be parsed
	#driver.get("https://www.websudoku.com/?")
	#time.sleep(5)
	#link=driver.find_element_by_xpath("/html/frameset/frame").get_attribute("src")
	#driver.get(link)
	
	#get sudoku from the website
	#table=parser.get_sudoku(driver,thread_name)
	
	#save the sudoku
	lock.acquire()
	save_sudoku(table_array,lock)
	lock.release()
	print(thread_name+" done.")

def save_sudoku(table,lock):
	
	parser.printTable(table,9,9)
	



driver=3
#driver=webdriver.Firefox()
create_workers(driver)

#driver.quit()











