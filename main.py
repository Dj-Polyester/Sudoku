import threading
from selenium import webdriver
import parser
import time
from multi_dim_array import MultiDimArray

#choose a number that can be divided four, in case there is equal distribution in the difficulty of puzzles
NUMBER_OF_THREADS=8
threads = []

# Create worker threads
def create_workers():
	lock=threading.Lock()
	for i in range(NUMBER_OF_THREADS):
		tmp="thread "+str(i+1)
		difficulty=int(i/2+1)
		t = threading.Thread(target=work,args=(lock,difficulty),name=tmp,daemon=True)
		threads.append(t)
		
		t.start()

def work(lock,difficulty):
	#open a browser window
	driver=webdriver.Firefox()
	
	#initialize class
	table=MultiDimArray(9,9," ")

	thread_name=threading.current_thread().name
	dif_keyword=translate_difficulty(difficulty)
	print(thread_name+" on "+ dif_keyword +" mode started.")

	#get the website to be parsed in terms of difficulty
	driver.get("https://www.websudoku.com/?level="+str(difficulty))
	time.sleep(5)
	
	#get over the frame
	link=driver.find_element_by_xpath("/html/frameset/frame").get_attribute("src")
	driver.get(link)

	#get sudoku from the website
	table_array=parser.get_sudoku(table,driver,thread_name)
	
	#save the sudoku
	lock.acquire()
	save_sudoku(table_array,lock,difficulty)
	lock.release()
	print(thread_name+" done.")

	#close the browser window
	driver.quit()

def save_sudoku(table_array,lock,difficulty):
	dif_keyword=translate_difficulty(difficulty)
	with open("{}.log".format(dif_keyword),"a+") as fileName:
		print(file=fileName)
		print("#{}".format(time.ctime()),file=fileName)
		parser.printToFile(table_array,9,9,fileName)

create_workers()

def translate_difficulty(difficulty):
	if difficulty==1: dif_keyword="easy"
	elif difficulty==2: dif_keyword="medium"
	elif difficulty==3: dif_keyword="hard"
	elif difficulty==4: dif_keyword="evil"
	else:
		print("Invalid difficulty level on [1,4]: {}".format(difficulty))
		exit(1)
	return dif_keyword

# for t in threads:
#     t.join()

# Inline version
[t.join() for t in threads]

print("main thread exited")

