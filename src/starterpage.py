# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'starterPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.page)
        self.widget.setMinimumSize(QtCore.QSize(921, 531))
        self.widget.setMaximumSize(QtCore.QSize(921, 531))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setMinimumSize(QtCore.QSize(400, 0))
        self.frame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame.setStyleSheet("QFrame#frame{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"border-radius: 30%\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 130, 243, 19))
        self.label.setStyleSheet("font: 75 12pt \"Arial\";\n"
"font-weight:550;\n"
"color: rgb(2, 50, 94);")
        self.label.setObjectName("label")
        self.signinstart = QtWidgets.QPushButton(self.frame)
        self.signinstart.setGeometry(QtCore.QRect(110, 190, 191, 31))
        self.signinstart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signinstart.setStyleSheet("*{color: rgb(2, 50, 94);\n"
"background-color: rgb(3, 143, 208);\n"
"border: opx;\n"
"border-radius: 12%;\n"
"font: 75 12pt \"Arial\";\n"
"font-weight:550;\n"
"}\n"
"::hover{\n"
"border: 2px solid rgb(3, 65, 124);\n"
"background-color: rgb(3, 65, 124);\n"
"    color: rgb(3, 175, 255);\n"
"\n"
"\n"
"}")
        self.signinstart.setObjectName("signinstart")
        self.signupstart = QtWidgets.QPushButton(self.frame)
        self.signupstart.setGeometry(QtCore.QRect(110, 250, 191, 31))
        self.signupstart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupstart.setStyleSheet("*{color: rgb(2, 50, 94);\n"
"background-color: rgb(3, 143, 208);\n"
"border: opx;\n"
"border-radius: 12%;\n"
"font: 75 12pt \"Arial\";\n"
"font-weight:550;\n"
"}\n"
"::hover{\n"
"border: 2px solid rgb(3, 65, 124);\n"
"background-color: rgb(3, 65, 124);\n"
"    color: rgb(3, 175, 255);\n"
"\n"
"\n"
"}")
        self.signupstart.setObjectName("signupstart")
        self.exitstart = QtWidgets.QPushButton(self.frame)
        self.exitstart.setGeometry(QtCore.QRect(110, 310, 191, 31))
        self.exitstart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitstart.setStyleSheet("*{color: rgb(2, 50, 94);\n"
"background-color: rgb(3, 143, 208);\n"
"border: opx;\n"
"border-radius: 12%;\n"
"font: 75 12pt \"Arial\";\n"
"font-weight:550;\n"
"}\n"
"::hover{\n"
"border: 2px solid rgb(3, 65, 124);\n"
"background-color: rgb(3, 65, 124);\n"
"    color: rgb(3, 175, 255);\n"
"\n"
"\n"
"}")
        self.exitstart.setObjectName("exitstart")
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_5 = QtWidgets.QWidget(self.page_2)
        self.widget_5.setMinimumSize(QtCore.QSize(921, 531))
        self.widget_5.setMaximumSize(QtCore.QSize(921, 531))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_8 = QtWidgets.QWidget(self.widget_5)
        self.widget_8.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.widget_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 30%;\n"
"border-bottom-left-radius: 30%;")
        self.widget_8.setObjectName("widget_8")
        self.label_15 = QtWidgets.QLabel(self.widget_8)
        self.label_15.setGeometry(QtCore.QRect(20, 30, 169, 40))
        self.label_15.setStyleSheet("font: 87 22pt \"Segoe UI\";\n"
"font-weight:600;")
        self.label_15.setObjectName("label_15")
        self.frame_8 = QtWidgets.QFrame(self.widget_8)
        self.frame_8.setGeometry(QtCore.QRect(70, 150, 300, 37))
        self.frame_8.setMinimumSize(QtCore.QSize(300, 37))
        self.frame_8.setMaximumSize(QtCore.QSize(300, 37))
        self.frame_8.setStyleSheet("QFrame#frame_8{\n"
"border: 2px solid rgb(5, 92, 175);\n"
"border-radius: 12%}\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setLineWidth(2)
        self.frame_8.setObjectName("frame_8")
        self.label_16 = QtWidgets.QLabel(self.frame_8)
        self.label_16.setGeometry(QtCore.QRect(12, 8, 20, 20))
        self.label_16.setMinimumSize(QtCore.QSize(20, 20))
        self.label_16.setMaximumSize(QtCore.QSize(20, 20))
        self.label_16.setStyleSheet("image: url(:/icons/assets/user.svg);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.userget = QtWidgets.QLineEdit(self.frame_8)
        self.userget.setGeometry(QtCore.QRect(37, 8, 250, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userget.sizePolicy().hasHeightForWidth())
        self.userget.setSizePolicy(sizePolicy)
        self.userget.setMinimumSize(QtCore.QSize(250, 20))
        self.userget.setMaximumSize(QtCore.QSize(250, 20))
        self.userget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.userget.setStyleSheet("font: 75 12pt \"Segoe UI\";\n"
"font-weight:550;")
        self.userget.setObjectName("userget")
        self.frame_9 = QtWidgets.QFrame(self.widget_8)
        self.frame_9.setGeometry(QtCore.QRect(70, 220, 300, 37))
        self.frame_9.setMinimumSize(QtCore.QSize(300, 37))
        self.frame_9.setMaximumSize(QtCore.QSize(300, 37))
        self.frame_9.setStyleSheet("QFrame#frame_9{\n"
"border: 2px solid rgb(5, 92, 175);\n"
"border-radius: 12%}\n"
"")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setLineWidth(2)
        self.frame_9.setObjectName("frame_9")
        self.label_17 = QtWidgets.QLabel(self.frame_9)
        self.label_17.setGeometry(QtCore.QRect(12, 8, 20, 20))
        self.label_17.setMinimumSize(QtCore.QSize(20, 20))
        self.label_17.setMaximumSize(QtCore.QSize(20, 20))
        self.label_17.setStyleSheet("image: url(:/icons/assets/key.svg);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.passget = QtWidgets.QLineEdit(self.frame_9)
        self.passget.setGeometry(QtCore.QRect(37, 8, 230, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passget.sizePolicy().hasHeightForWidth())
        self.passget.setSizePolicy(sizePolicy)
        self.passget.setMinimumSize(QtCore.QSize(230, 20))
        self.passget.setMaximumSize(QtCore.QSize(230, 20))
        self.passget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.passget.setStyleSheet("font: 75 12pt \"Segoe UI\";\n"
"font-weight:550;\n"
"")
        self.passget.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passget.setObjectName("passget")
        self.showhide = QtWidgets.QPushButton(self.frame_9)
        self.showhide.setGeometry(QtCore.QRect(270, 7, 23, 23))
        self.showhide.setStyleSheet("QPushButton#showhide{\n"
"    \n"
"    image: url(:/icons/assets/show_key.svg);\n"
"}\n"
"QPushButton#showhide::checked{\n"
"    \n"
"    image: url(:/icons/assets/hide_key.svg);\n"
"}")
        self.showhide.setText("")
        self.showhide.setCheckable(True)
        self.showhide.setObjectName("showhide")
        self.signinbtn = QtWidgets.QPushButton(self.widget_8)
        self.signinbtn.setGeometry(QtCore.QRect(130, 330, 181, 31))
        self.signinbtn.setMinimumSize(QtCore.QSize(181, 31))
        self.signinbtn.setMaximumSize(QtCore.QSize(181, 31))
        self.signinbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signinbtn.setStyleSheet("QPushButton#signinbtn{\n"
"        border: 2px solid qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    border-radius: 12%;\n"
"    font: 75 12pt \"Segoe UI\";\n"
"    font-weight: 550;\n"
"    color: rgb(5, 92, 175);\n"
"}\n"
"QPushButton#signinbtn::hover{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.signinbtn.setObjectName("signinbtn")
        self.forgetpass = QtWidgets.QLabel(self.widget_8)
        self.forgetpass.setGeometry(QtCore.QRect(260, 270, 109, 16))
        self.forgetpass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgetpass.setStyleSheet("QLabel#forgetpass{\n"
"font: 10pt \"Arial\";\n"
"    color: rgb(3, 143, 208);\n"
"}\n"
"QLabel#forgetpass::hover{\n"
"    \n"
"    font: 87 10pt \"Arial\";\n"
"    font-weight:800;\n"
"    color: rgb(5, 92, 175);\n"
"}")
        self.forgetpass.setObjectName("forgetpass")
        self.backbtn = QtWidgets.QPushButton(self.widget_8)
        self.backbtn.setGeometry(QtCore.QRect(130, 380, 181, 31))
        self.backbtn.setMinimumSize(QtCore.QSize(181, 31))
        self.backbtn.setMaximumSize(QtCore.QSize(181, 31))
        self.backbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backbtn.setStyleSheet("QPushButton#backbtn{\n"
"        border: 2px solid qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    border-radius: 12%;\n"
"    font: 75 12pt \"Segoe UI\";\n"
"    font-weight: 550;\n"
"    color: rgb(5, 92, 175);\n"
"}\n"
"QPushButton#backbtn::hover{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.backbtn.setObjectName("backbtn")
        self.horizontalLayout_7.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget_5)
        self.widget_9.setStyleSheet("QWidget#widget_9{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    border-top-right-radius: 30%;\n"
"    border-bottom-right-radius: 30%;\n"
"}")
        self.widget_9.setObjectName("widget_9")
        self.label_19 = QtWidgets.QLabel(self.widget_9)
        self.label_19.setGeometry(QtCore.QRect(50, 40, 366, 43))
        self.label_19.setStyleSheet("font: 26pt \"Impact\"; color: white")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.widget_9)
        self.label_20.setGeometry(QtCore.QRect(100, 130, 281, 271))
        self.label_20.setMinimumSize(QtCore.QSize(281, 271))
        self.label_20.setMaximumSize(QtCore.QSize(281, 271))
        self.label_20.setStyleSheet("image: url(:/icons/assets/login.png);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_7.addWidget(self.widget_9)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.page_3)
        self.widget_2.setMinimumSize(QtCore.QSize(921, 531))
        self.widget_2.setMaximumSize(QtCore.QSize(921, 531))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setStyleSheet("QWidget#widget_3{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    border-top-left-radius: 30%;\n"
"    border-bottom-left-radius: 30%;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 294, 43))
        self.label_2.setStyleSheet("font: 26pt \"Impact\"; color: white")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(100, 130, 281, 271))
        self.label_7.setMinimumSize(QtCore.QSize(281, 271))
        self.label_7.setMaximumSize(QtCore.QSize(281, 271))
        self.label_7.setStyleSheet("image: url(:/icons/assets/signup.png);")
        self.label_7.setText("")
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(451, 513))
        self.widget_4.setMaximumSize(QtCore.QSize(451, 513))
        self.widget_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 30%;\n"
"border-bottom-right-radius: 30%;")
        self.widget_4.setObjectName("widget_4")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setGeometry(QtCore.QRect(9, 22, 182, 40))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_3.setStyleSheet("font: 87 22pt \"Segoe UI\";\n"
"font-weight:600;")
        self.label_3.setObjectName("label_3")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.widget_4)
        self.stackedWidget_2.setGeometry(QtCore.QRect(9, 91, 421, 400))
        self.stackedWidget_2.setMinimumSize(QtCore.QSize(421, 381))
        self.stackedWidget_2.setMaximumSize(QtCore.QSize(421, 400))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.frame_2 = QtWidgets.QFrame(self.page_4)
        self.frame_2.setGeometry(QtCore.QRect(70, 70, 300, 37))
        self.frame_2.setMinimumSize(QtCore.QSize(300, 37))
        self.frame_2.setMaximumSize(QtCore.QSize(300, 37))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"border: 2px solid rgb(5, 92, 175);\n"
"border-radius: 12%}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(12, 8, 20, 20))
        self.label_4.setMinimumSize(QtCore.QSize(20, 20))
        self.label_4.setMaximumSize(QtCore.QSize(20, 20))
        self.label_4.setStyleSheet("image: url(:/icons/assets/user.svg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.usercreate = QtWidgets.QLineEdit(self.frame_2)
        self.usercreate.setGeometry(QtCore.QRect(37, 8, 250, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usercreate.sizePolicy().hasHeightForWidth())
        self.usercreate.setSizePolicy(sizePolicy)
        self.usercreate.setMinimumSize(QtCore.QSize(250, 20))
        self.usercreate.setMaximumSize(QtCore.QSize(250, 20))
        self.usercreate.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.usercreate.setStyleSheet("font: 75 12pt \"Segoe UI\";\n"
"font-weight:550;")
        self.usercreate.setObjectName("usercreate")
        self.frame_3 = QtWidgets.QFrame(self.page_4)
        self.frame_3.setGeometry(QtCore.QRect(70, 130, 300, 37))
        self.frame_3.setMinimumSize(QtCore.QSize(300, 37))
        self.frame_3.setMaximumSize(QtCore.QSize(300, 37))
        self.frame_3.setStyleSheet("QFrame#frame_3{\n"
"border: 2px solid rgb(5, 92, 175);\n"
"border-radius: 12%}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(7, 7, 27, 27))
        self.label_5.setMinimumSize(QtCore.QSize(27, 27))
        self.label_5.setMaximumSize(QtCore.QSize(27, 27))
        self.label_5.setStyleSheet("image: url(:/icons/assets/mail.svg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.emailcreate = QtWidgets.QLineEdit(self.frame_3)
        self.emailcreate.setGeometry(QtCore.QRect(37, 8, 250, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailcreate.sizePolicy().hasHeightForWidth())
        self.emailcreate.setSizePolicy(sizePolicy)
        self.emailcreate.setMinimumSize(QtCore.QSize(250, 20))
        self.emailcreate.setMaximumSize(QtCore.QSize(250, 20))
        self.emailcreate.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.emailcreate.setStyleSheet("font: 75 12pt \"Segoe UI\";\n"
"font-weight:550;")
        self.emailcreate.setObjectName("emailcreate")
        self.nextbtn = QtWidgets.QPushButton(self.page_4)
        self.nextbtn.setGeometry(QtCore.QRect(130, 200, 181, 31))
        self.nextbtn.setMinimumSize(QtCore.QSize(181, 31))
        self.nextbtn.setMaximumSize(QtCore.QSize(181, 31))
        self.nextbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextbtn.setStyleSheet("QPushButton#nextbtn{\n"
"        border: 2px solid qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    border-radius: 12%;\n"
"    font: 75 12pt \"Segoe UI\";\n"
"    font-weight: 550;\n"
"    color: rgb(5, 92, 175);\n"
"}\n"
"QPushButton#nextbtn::hover{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.nextbtn.setObjectName("nextbtn")
        self.backbtn2 = QtWidgets.QPushButton(self.page_4)
        self.backbtn2.setGeometry(QtCore.QRect(130, 250, 181, 31))
        self.backbtn2.setMinimumSize(QtCore.QSize(181, 31))
        self.backbtn2.setMaximumSize(QtCore.QSize(181, 31))
        self.backbtn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backbtn2.setStyleSheet("QPushButton#backbtn2{\n"
"        border: 2px solid qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    border-radius: 12%;\n"
"    font: 75 12pt \"Segoe UI\";\n"
"    font-weight: 550;\n"
"    color: rgb(5, 92, 175);\n"
"}\n"
"QPushButton#backbtn2::hover{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.backbtn2.setObjectName("backbtn2")
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.frame_4 = QtWidgets.QFrame(self.page_5)
        self.frame_4.setGeometry(QtCore.QRect(70, 70, 300, 37))
        self.frame_4.setMinimumSize(QtCore.QSize(300, 37))
        self.frame_4.setMaximumSize(QtCore.QSize(300, 37))
        self.frame_4.setStyleSheet("QFrame#frame_4{\n"
"border: 2px solid rgb(5, 92, 175);\n"
"border-radius: 12%}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.frame_4.setObjectName("frame_4")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(12, 8, 20, 20))
        self.label_8.setMinimumSize(QtCore.QSize(20, 20))
        self.label_8.setMaximumSize(QtCore.QSize(20, 20))
        self.label_8.setStyleSheet("image: url(:/icons/assets/key.svg);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pascreate = QtWidgets.QLineEdit(self.frame_4)
        self.pascreate.setGeometry(QtCore.QRect(37, 8, 230, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pascreate.sizePolicy().hasHeightForWidth())
        self.pascreate.setSizePolicy(sizePolicy)
        self.pascreate.setMinimumSize(QtCore.QSize(230, 20))
        self.pascreate.setMaximumSize(QtCore.QSize(230, 20))
        self.pascreate.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pascreate.setStyleSheet("font: 75 12pt \"Segoe UI\";\n"
"font-weight:550;")
        self.pascreate.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pascreate.setObjectName("pascreate")
        self.showhide2 = QtWidgets.QPushButton(self.frame_4)
        self.showhide2.setGeometry(QtCore.QRect(270, 7, 23, 23))
        self.showhide2.setStyleSheet("QPushButton#showhide2{\n"
"    \n"
"    image: url(:/icons/assets/show_key.svg);\n"
"}\n"
"QPushButton#showhide2::checked{\n"
"    \n"
"    image: url(:/icons/assets/hide_key.svg);\n"
"}")
        self.showhide2.setText("")
        self.showhide2.setCheckable(True)
        self.showhide2.setObjectName("showhide2")
        self.signinbtn_2 = QtWidgets.QPushButton(self.page_5)
        self.signinbtn_2.setGeometry(QtCore.QRect(130, 200, 181, 31))
        self.signinbtn_2.setMinimumSize(QtCore.QSize(181, 31))
        self.signinbtn_2.setMaximumSize(QtCore.QSize(181, 31))
        self.signinbtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signinbtn_2.setStyleSheet("QPushButton#signinbtn_2{\n"
"        border: 2px solid qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    border-radius: 12%;\n"
"    font: 75 12pt \"Segoe UI\";\n"
"    font-weight: 550;\n"
"    color: rgb(5, 92, 175);\n"
"}\n"
"QPushButton#signinbtn_2::hover{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 90, 174, 255), stop:1 rgba(3, 147, 212, 255));\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.signinbtn_2.setObjectName("signinbtn_2")
        self.frame_5 = QtWidgets.QFrame(self.page_5)
        self.frame_5.setGeometry(QtCore.QRect(70, 130, 300, 37))
        self.frame_5.setMinimumSize(QtCore.QSize(300, 37))
        self.frame_5.setMaximumSize(QtCore.QSize(300, 37))
        self.frame_5.setStyleSheet("QFrame#frame_5{\n"
"border: 2px solid rgb(5, 92, 175);\n"
"border-radius: 12%}\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(12, 8, 20, 20))
        self.label_11.setMinimumSize(QtCore.QSize(20, 20))
        self.label_11.setMaximumSize(QtCore.QSize(20, 20))
        self.label_11.setStyleSheet("image: url(:/icons/assets/key.svg);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.conpascreate = QtWidgets.QLineEdit(self.frame_5)
        self.conpascreate.setGeometry(QtCore.QRect(37, 8, 230, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conpascreate.sizePolicy().hasHeightForWidth())
        self.conpascreate.setSizePolicy(sizePolicy)
        self.conpascreate.setMinimumSize(QtCore.QSize(230, 20))
        self.conpascreate.setMaximumSize(QtCore.QSize(230, 20))
        self.conpascreate.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.conpascreate.setStyleSheet("font: 75 12pt \"Segoe UI\";\n"
"font-weight:550;")
        self.conpascreate.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conpascreate.setObjectName("conpascreate")
        self.showhide3 = QtWidgets.QPushButton(self.frame_5)
        self.showhide3.setGeometry(QtCore.QRect(270, 7, 23, 23))
        self.showhide3.setStyleSheet("QPushButton#showhide3{\n"
"    \n"
"    image: url(:/icons/assets/show_key.svg);\n"
"}\n"
"QPushButton#showhide3::checked{\n"
"    \n"
"    image: url(:/icons/assets/hide_key.svg);\n"
"}")
        self.showhide3.setText("")
        self.showhide3.setCheckable(True)
        self.showhide3.setObjectName("showhide3")
        self.stackedWidget_2.addWidget(self.page_5)
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Continue with your account, Via"))
        self.signinstart.setText(_translate("MainWindow", "Sign-In"))
        self.signupstart.setText(_translate("MainWindow", "Sign-Up"))
        self.exitstart.setText(_translate("MainWindow", "Exit"))
        self.label_15.setText(_translate("MainWindow", "Signin Here!"))
        self.userget.setPlaceholderText(_translate("MainWindow", "User-Id"))
        self.passget.setPlaceholderText(_translate("MainWindow", "Password"))
        self.signinbtn.setText(_translate("MainWindow", "Sign-In"))
        self.forgetpass.setText(_translate("MainWindow", "Forget Password ?"))
        self.backbtn.setText(_translate("MainWindow", "Back"))
        self.label_19.setText(_translate("MainWindow", "WELCOME BACK TO SIGN-IN"))
        self.label_2.setText(_translate("MainWindow", "WELCOME TO SIGN-UP"))
        self.label_3.setText(_translate("MainWindow", "SignUp Here!"))
        self.usercreate.setPlaceholderText(_translate("MainWindow", "User-Id"))
        self.emailcreate.setPlaceholderText(_translate("MainWindow", "E-Mail"))
        self.nextbtn.setText(_translate("MainWindow", "Next"))
        self.backbtn2.setText(_translate("MainWindow", "Back"))
        self.pascreate.setPlaceholderText(_translate("MainWindow", "Password"))
        self.signinbtn_2.setText(_translate("MainWindow", "Sign-In"))
        self.conpascreate.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())