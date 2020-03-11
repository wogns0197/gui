import sys,os,shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QProgressBar
from cr2_01 import Ui_MainWindow


class Example(QMainWindow,Ui_MainWindow):
	d1 = ""
	d2 = ""

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
	
	def findDir(self):
		options = QFileDialog.Option()
		options |= QFileDialog.ShowDirsOnly
		working_path1 = QFileDialog.getExistingDirectory(self,"select Dir")
		global d1
		d1 = working_path1
		self.label_3.setText(working_path1)
		print(d1)
		
		
	def findDir2(self):
		options = QFileDialog.Option()
		options |= QFileDialog.ShowDirsOnly
		working_path2 = QFileDialog.getExistingDirectory(self,"select Dir")
		global d2
		d2 = working_path2
		self.label_4.setText(working_path2)
		print(d2)
	def accept():
		pass
	
	def go(self):
		
		
		self.count = 1
		self.num = 1
		global d1,d2
		# d1 = "/Users/kwonjaehoon/Documents/python/hs/jpeg"
		# d2 = "/Users/kwonjaehoon/Documents/python/hs/cr2"
		
		if(d1!="" and d2!=""):
			
			path_j = d1
			path_cr = d2

			file_list_jp = os.listdir(path_j)
			file_list_cr = os.listdir(path_cr)
			

			if( not os.path.isdir("./output")):
				dir_path = "./"
				dir_name = "output"
				os.mkdir(dir_path + "/" + dir_name + "/")
			

			for i in file_list_jp :	

				for j in file_list_cr:
					if (i[:-4] == j[:-4]):
						self.progressBar.setValue(self.count)
						self.count += int(100/len(file_list_jp))+1
						self.num += 1
						print(self.count)
						shutil.copy(d2+'/'+j , 'output')
						if(self.num == len(file_list_jp)):
							self.progressBar.setValue(100)
							self.label_7.setText("작업종료! 폴더가 생성되었습니다")

			
		
			
		
		
app = QApplication([])
ex = Example()

sys.exit(app.exec_())