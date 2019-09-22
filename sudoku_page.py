from selenium import webdriver

class Driver:
    def __init__(self):
        self.window=webdriver.Firefox()
    
    def closeBrowser(self):
		self.window.close()
    