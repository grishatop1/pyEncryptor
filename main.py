from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from encryption import encryptFiles
from encryption import decryptFiles
from threading import Thread
import ntpath
import os


class Ui_MainWindow(object):
	def __init__(self):
		self.selected_files_enc = []
		self.selected_files_dec = []

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setEnabled(True)
		MainWindow.setFixedSize(400, 370)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.header = QtWidgets.QLabel(self.centralwidget)
		self.header.setGeometry(QtCore.QRect(0, 0, 401, 41))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.header.setFont(font)
		self.header.setAlignment(QtCore.Qt.AlignCenter)
		self.header.setObjectName("header")
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(200, 80, 3, 270))
		self.line.setFrameShape(QtWidgets.QFrame.VLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.password = QtWidgets.QLineEdit(self.centralwidget)
		self.password.setGeometry(QtCore.QRect(90, 50, 231, 20))
		self.password.setObjectName("password")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 160, 271))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label_encrpyt = QtWidgets.QLabel(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_encrpyt.setFont(font)
		self.label_encrpyt.setAlignment(QtCore.Qt.AlignCenter)
		self.label_encrpyt.setObjectName("label_encrpyt")
		self.verticalLayout.addWidget(self.label_encrpyt)
		self.select_encrypt = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.select_encrypt.setObjectName("select_encrypt")
		self.select_encrypt.clicked.connect(self.selectFilesEnc)
		self.verticalLayout.addWidget(self.select_encrypt)
		self.label_select1 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_select1.setAlignment(QtCore.Qt.AlignCenter)
		self.label_select1.setObjectName("label_select1")
		self.verticalLayout.addWidget(self.label_select1)
		self.files_encrpyt = QtWidgets.QListWidget(self.verticalLayoutWidget)
		self.files_encrpyt.setObjectName("files_encrpyt")
		self.verticalLayout.addWidget(self.files_encrpyt)
		self.encrypt_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.encrypt_button.setObjectName("encrypt_button")
		self.encrypt_button.clicked.connect(self.encrypt)
		self.verticalLayout.addWidget(self.encrypt_button)
		self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 80, 160, 271))
		self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label_decrpyt = QtWidgets.QLabel(self.verticalLayoutWidget_2)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_decrpyt.setFont(font)
		self.label_decrpyt.setAlignment(QtCore.Qt.AlignCenter)
		self.label_decrpyt.setObjectName("label_decrpyt")
		self.verticalLayout_2.addWidget(self.label_decrpyt)
		self.select_decrypt = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
		self.select_decrypt.setObjectName("select_decrypt")
		self.select_decrypt.clicked.connect(self.selectFilesDec)
		self.verticalLayout_2.addWidget(self.select_decrypt)
		self.label_select2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
		self.label_select2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_select2.setObjectName("label_select2")
		self.verticalLayout_2.addWidget(self.label_select2)
		self.files_decrpyt = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
		self.files_decrpyt.setWordWrap(True)
		self.files_decrpyt.setObjectName("files_decrpyt")
		self.verticalLayout_2.addWidget(self.files_decrpyt)
		self.decrypt_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
		self.decrypt_button.setObjectName("decrypt_button")
		self.decrypt_button.clicked.connect(self.decrypt)
		self.verticalLayout_2.addWidget(self.decrypt_button)

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.header.setText(_translate("MainWindow", "Encryptor"))
		self.password.setPlaceholderText(_translate("MainWindow", "Enter password"))
		self.label_encrpyt.setText(_translate("MainWindow", "Encrypt Files"))
		self.select_encrypt.setText(_translate("MainWindow", "Select files..."))
		self.label_select1.setText(_translate("MainWindow", "Selected files:"))
		self.encrypt_button.setText(_translate("MainWindow", "Encrypt!"))
		self.label_decrpyt.setText(_translate("MainWindow", "Decrypt Files"))
		self.select_decrypt.setText(_translate("MainWindow", "Select files..."))
		self.label_select2.setText(_translate("MainWindow", "Selected files:"))
		self.decrypt_button.setText(_translate("MainWindow", "Decrypt!"))

	def resetButtonEnc(self):
		self.encrypt_button.setText("Encrypt!")
		self.encrypt_button.setStyleSheet("color: black;")
		self.encrypt_button.setDisabled(False)

	def resetButtonDec(self):
		self.decrypt_button.setText("Decrypt!")
		self.decrypt_button.setStyleSheet("color: black;")
		self.decrypt_button.setDisabled(False)

	def selectFilesEnc(self):
		self.selected_files_enc, _ = QFileDialog.getOpenFileNames(None, "Select files to encrypt")
		self.files_encrpyt.clear()
		for file in self.selected_files_enc:
			self.files_encrpyt.addItem(ntpath.basename(file))

		self.resetButtonEnc()

	def selectFilesDec(self):
		self.selected_files_dec, _ = QFileDialog.getOpenFileNames(None, "Select files to decrypt", "", "CRY Files (*.cry)")
		self.files_decrpyt.clear()
		for file in self.selected_files_dec:
			self.files_decrpyt.addItem(ntpath.basename(file))

		self.resetButtonDec()

	def encrypt(self):
		if not self.password.text():
			self.encrypt_button.setText("Enter password!")
			self.encrypt_button.setStyleSheet("color: red;")
			return

		if not self.selected_files_enc:
			self.encrypt_button.setText("Select files!")
			self.encrypt_button.setStyleSheet("color: red;")
			return

		self.encrypt_button.setText("Encrypting...")
		self.encrypt_button.setStyleSheet("color: green;")
		self.encrypt_button.setDisabled(True)

		Thread(target=encryptFiles, args=(self.selected_files_enc,self.password.text(), self), daemon=True).start()

	def decrypt(self):
		if not self.password.text():
			self.decrypt_button.setText("Enter password!")
			self.decrypt_button.setStyleSheet("color: red;")
			return

		if not self.selected_files_dec:
			self.decrypt_button.setText("Select files!")
			self.decrypt_button.setStyleSheet("color: red;")
			return

		self.decrypt_button.setText("Decrypting...")
		self.decrypt_button.setStyleSheet("color: green;")
		self.decrypt_button.setDisabled(True)

		Thread(target=decryptFiles, args=(self.selected_files_dec,self.password.text(), self), daemon=True).start()


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
