from PyQt5 import QtCore, QtGui, QtWidgets


class textEdit(QtWidgets.QTextEdit):
	def __init__(self,**kwargs):
		super().__init__()
		self.start=kwargs["start"]
		self.width=kwargs["width"]
		self.i=kwargs["i"]
		self.j=kwargs["j"]
		self.centralwidget=kwargs["centralwidget"]
		self.edit = QtWidgets.QTextEdit(self.centralwidget)
		self.edit.setGeometry(QtCore.QRect(self.start+self.i*self.width, self.width+self.j*self.width, self.width, self.width))
		self.edit.setObjectName("textEdit_"+str(self.j*9+self.i))
		# this calls self.fitText when text changes
		# and self.fitText changes text and thus gets called again
		# so we need to block signals in self.fitText
		self.edit.textChanged.connect(self.fitText)   
		
		font = QtGui.QFont()
		font.setPointSize(26)
		self.edit.setFont(font)
		self.edit.setAlignment(QtCore.Qt.AlignCenter)

	def fitText(self):
		#get the text element
		text = self.edit.toPlainText()

		if text.isnumeric()==False:
			text=""
		if len(text) > 1:
			text=text[:1]

		# block signals to prevent RecursionError
		self.edit.blockSignals(True)
		#set to the specified element
		self.edit.setPlainText(text)
		# return to previous state
		self.edit.blockSignals(False)
