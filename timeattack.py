import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class Timer(object):
	def __init__(self):
		self.sethour = 0
		self.setmin = 0
		self.setsec = 0

	def setHour(self,shour): self.sethour = shour
	def setMin(self,smin): self.setmin = smin
	def setSec(self,ssec): self.setsec = ssec	

class GUITimer(QWidget,Timer):
	def __init__(self):
		super().__init__()
		self.initUI()

	def setTime(self):
		self.setHour(int(self.GUIhour.text()))
		self.setMin(int(self.GUImin.text()))
		self.setSec(int(self.GUIsec.text()))
		
	def AddSet(self,grid,a,b,c,number):
		grid.addWidget(a,number,0)
		grid.addWidget(b,number,1)
		grid.addWidget(c,number,2)

	def timer(self,grid):
		k = 3
		while self.sethour != 0 or self.setmin != 0 or self.setsec != 0:
			time.sleep(1)
			(GUIhour,GUImin,GUIsec) = (QLabel(str(sethour)),QLabel(str(self.setmin)),QLabel(str(self.setsec)))
			self.AddSet(grid,GUIhour,GUImin,GUIsec,k)
			k += 1
			self.setsec -= 1
			if (self.setsec == 0 and self.setmin != 0):
				self.setmin -= 1
				self.setsec = 60
			if (self.setmin ==0 and self.sethour != 0):
				self.setmin = 60
				self.sethour -= 1

	def initUI(self):
		grid = QGridLayout()
		grid.setSpacing(10)
		(tempH,tempM,tempS) = (QLabel("Hour"),QLabel("Min"),QLabel("Sec"))
		tempH.setAlignment(Qt.AlignCenter)
		tempM.setAlignment(Qt.AlignCenter)
		tempS.setAlignment(Qt.AlignCenter)
		self.AddSet(grid,tempH,tempM,tempS,0)
		(self.GUIhour,self.GUImin,self.GUIsec) = (QLineEdit(),QLineEdit(),QLineEdit())
		self.AddSet(grid,self.GUIhour,self.GUImin,self.GUIsec,1)
		submit = QPushButton("SUBMIT",self)
		submit.clicked.connect(self.setTime)
		grid.addWidget(submit,1,3)
		self.timer(grid)
		self.setLayout(grid) 
		self.setGeometry(300, 300, 100, 100)
		self.setWindowTitle('Show Commit')	
		self.show()

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = GUITimer()
	sys.exit(app.exec_())
