import threading
import time 

NUMBER_OF_THREADS=8


# Create worker threads (will die when main exits)
def create_workers():
    for i in range(NUMBER_OF_THREADS):
        tmp="thread "+str(i+1)
        t = threading.Thread(target=work,name=tmp,daemon=True)
        t.start()

def work():
    print("yoman")


create_workers()