import sys, re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pymongo import MongoClient

from starterpage import Ui_MainWindow

class MainPage(QMainWindow):
	def __init__(self):
		super().__init__()

		# todo: initial setup for ui
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.stackedWidget.setCurrentIndex(0)

		# todo: create func for options page
		self.ui.signinstart.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
		self.ui.signupstart.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

		# todo: create db connection
		global col
		self.con = MongoClient("mongodb://127.0.0.1:27017")
		self.db = self.con['PYQT5-LOGINPAGE']
		self.col = self.db['USERS']

		# todo: create func for signin-page
		# todo: create func for back-button
		self.ui.backbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))	
		
		# todo: create func for signin-button
		self.ui.signinbtn.clicked.connect(lambda: self.signIn(
			self.ui.userget,
			self.ui.passget
			))	

		# todo: create func for hide/show keys
		self.ui.showhide.clicked.connect(lambda:self.showKey(self.ui.passget))

		# todo: create func for signup-page
		# todo: create func for back-button
		self.ui.backbtn2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

		# todo: create func for next-button
		self.ui.nextbtn.clicked.connect(lambda: self.nextPage(
			self.ui.usercreate,
			self.ui.emailcreate
			))

		# todo: create func for signup-button
		self.ui.signinbtn_2.clicked.connect(lambda:self.signUp(
			self.ui.usercreate,
			self.ui.emailcreate,
			self.ui.pascreate,
			self.ui.conpascreate
			))

		# todo: create func for hide/show keys
		self.ui.showhide2.clicked.connect(lambda:self.showKey2(self.ui.pascreate))
		self.ui.showhide3.clicked.connect(lambda:self.showKey3(self.ui.conpascreate))

		# todo: creaet func for exit-Button
		self.ui.exitstart.clicked.connect(self.exitFunc)

	def exitFunc(self):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Warning)
		msg.setText("Are you sure to want exit?")
		msg.setWindowTitle("Error")
		msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.No | QMessageBox.Yes)
		exe = msg.exec_()
		if exe == QMessageBox.Yes:
			self.close()
		else:
			return None

	def showKey3(self, conpascreate):
		if self.ui.showhide3.isChecked():
			self.ui.conpascreate.setEchoMode(QLineEdit.Normal)
		else:
			self.ui.conpascreate.setEchoMode(QLineEdit.Password)

	def showKey2(self, pascreate):
		if self.ui.showhide2.isChecked():
			self.ui.pascreate.setEchoMode(QLineEdit.Normal)
		else:
			self.ui.pascreate.setEchoMode(QLineEdit.Password)

	def showKey(self, conpascreate):
		if self.ui.showhide.isChecked():
			self.ui.passget.setEchoMode(QLineEdit.Normal)
		else:
			self.ui.passget.setEchoMode(QLineEdit.Password)

	def signIn(self, userget, passget):
		global col
		if self.ui.userget.text() == "" or self.ui.passget.text() == "":
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Critical)
			msg.setText("Something went wrong.Try again")
			msg.setWindowTitle("Error")
			msg.setStandardButtons(QMessageBox.Ok)
			exe = msg.exec_()
		else:
			match_data = {
			"user": self.ui.userget.text(),
			"passwd": self.ui.passget.text()
			}
			result = self.col.find(match_data)
			if result:
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Information)
				msg.setText(f"' {self.ui.userget.text()} ' profile Logged successfully.")
				msg.setWindowTitle("Information")
				msg.setStandardButtons(QMessageBox.Ok)
				exe = msg.exec_()
				if exe == QMessageBox.Ok:
					self.ui.userget.clear()
					self.ui.passget.clear()
					self.ui.stackedWidget.setCurrentIndex(0)
				else:
					return result


	def signUp(self, usercreate, emailcreate, pascreate, conpascreate):
		global col
		if self.ui.pascreate.text() == "" or self.ui.conpascreate.text() == "":
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Critical)
			msg.setText("Password are mismatch.Try again")
			msg.setWindowTitle("Error")
			msg.setStandardButtons(QMessageBox.Ok)
			exe = msg.exec_()
		else:
			data = {
			"user":self.ui.usercreate.text(),
			"email":self.ui.emailcreate.text(),
			"passwd":self.ui.conpascreate.text()
			}
			result = self.col.insert_one(data)
			if result:
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Information)
				msg.setText(f"' {self.ui.usercreate.text()} ' profile created successfully.")
				msg.setWindowTitle("Information")
				msg.setStandardButtons(QMessageBox.Ok)
				exe = msg.exec_()
				if exe == QMessageBox.Ok:
					self.ui.usercreate.clear()
					self.ui.emailcreate.clear()
					self.ui.pascreate.clear()
					self.ui.conpascreate.clear()
					self.ui.stackedWidget.setCurrentIndex(0)
				else:
					return result

	def nextPage(self, usercreate, emailcreate):
		global col 
		if self.ui.usercreate.text() == '' or self.ui.emailcreate.text() == '':
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Critical)
			msg.setText("Something went wrong.Try again")
			msg.setWindowTitle("Error")
			msg.setStandardButtons(QMessageBox.Ok)
			exe = msg.exec_()
		else:
			regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
			if(re.fullmatch(regex, self.ui.emailcreate.text())):
				usr_find = self.col.find_one({"user":self.ui.usercreate.text()})
				email_find = self.col.find_one({"email":self.ui.emailcreate.text()})
				if usr_find:
					msg = QMessageBox()
					msg.setIcon(QMessageBox.Critical)
					msg.setText("UserID already exists.Try with different one.")
					msg.setWindowTitle("Error")
					msg.setStandardButtons(QMessageBox.Ok)
					exe = msg.exec_()
				elif email_find:
					msg = QMessageBox()
					msg.setIcon(QMessageBox.Critical)
					msg.setText("Email-ID already exists.Try with different one.")
					msg.setWindowTitle("Error")
					msg.setStandardButtons(QMessageBox.Ok)
					exe = msg.exec_()
				else:
					self.ui.stackedWidget_2.setCurrentIndex(1)

			else:
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Critical)
				msg.setText("Email-Id is invalid.Try with different one.")
				msg.setWindowTitle("Error")
				msg.setStandardButtons(QMessageBox.Ok)
				exe = msg.exec_()

def main():
	app = QApplication(sys.argv)
	m = MainPage()
	m.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
