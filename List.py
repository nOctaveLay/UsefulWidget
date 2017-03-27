from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import datetime
# Van-st
#not finished yet
import time
class Ui_Form(object):
	def setupUi(self,Form):
		w = 400
		h = 300
		self.grid = QGridLayout()
		Form.setObjectName("Form")
		Form.resize(w,h)
		Form.setLayout(self.grid)
		Form.setWindowTitle('time running')
		self.label = QLabel(Form)
		self.label.setAlignment(Qt.AlignCenter)
		# self.label.setGeometry(QRect(0,0,w,h))#x,y,w,h text is printed on left bottom of box
		self.label.setObjectName("label")
		self.grid.addWidget(self.label,0,0)

		self.Push = QPushButton("start",Form)
		self.grid.addWidget(self.Push,1,0)

class MainControl(object):
	def __init__(self,time):
		self.start_time = time
		self.count_time = 0
	def run(self):
		while True:
			input_sen = input("if you finish the work, you must input the message 'end': ")
			# if input_sen == 'a':
			# 	sum_list += 10
			if input_sen == 'end':
				end_time = time.time()
				delta_time = round(end_time - self.start_time,0)
				delta_hour = int(delta_time // 60 // 60)
				delta_min = int((delta_time // 60 )% 60)
				delta_sec = int(delta_time % 60)
				self.text1 = "Running time ",str(delta_hour)+":"+str(delta_min)+":"+str(delta_sec)
				# self.text2 = "The score is"+sum_list
				break
			# print("plus the score ")

if __name__ == "__main__":
	start_time = time.time()
	file__ = open("running_time.txt","a")
	app = QApplication(sys.argv)
	Form = QWidget()
	ui = Ui_Form()
	control = MainControl(start_time)
	ui.setupUi(Form)
	Form.show()
	def update_label():
		count = control.count_time
		count_hour = int(count // 60 // 60)
		count_min = int((count // 60) % 60)
		count_sec = int(count % 60)
		ui.label.setText("running time is "+str(count_hour)+":"+str(count_min)+":"+str(count_sec))
		control.count_time += 1
	timer = QTimer()
	timer.timeout.connect(update_label)
	def time_start():
		timer.start(1000)
	ui.Push.clicked.connect(time_start)
	if app.exec_() == 0:
		count = control.count_time
		file__.write(str({'date':datetime.datetime.now(),'hour':int(count//60//60),'min':int((count//60)%60),'sec':int(count%60)})+"\n")
		file__.close()
		sys.exit()