import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MOS(object):
    def setupUi(self, MOS):
        MOS.setObjectName("MOS")
        MOS.resize(1059, 610)
        MOS.setStyleSheet("background-color:rgb(15, 128, 255)")
        self.centralwidget = QtWidgets.QWidget(MOS)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton_1_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1_home.setStyleSheet("background-color:rgb(15, 128, 255);color:rgb(255, 255, 255);border:1px groove gray;border-radius:10px;padding:2px 9px;border-style: outset;\n"
"")
        self.pushButton_1_home.setObjectName("pushButton_1_home")
        self.gridLayout.addWidget(self.pushButton_1_home, 0, 2, 1, 1)
        self.pushButton_5_about = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5_about.setStyleSheet("background-color:rgb(15, 128, 255);color:rgb(255, 255, 255);border:1px groove gray;border-radius:10px;padding:2px 9px;border-style: outset;")
        self.pushButton_5_about.setObjectName("pushButton_5_about")
        self.gridLayout.addWidget(self.pushButton_5_about, 0, 6, 1, 1)
        self.pushButton_4_shezhi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4_shezhi.setStyleSheet("background-color:rgb(15, 128, 255);color:rgb(255, 255, 255);border:1px groove gray;border-radius:10px;padding:2px 9px;border-style: outset;")
        self.pushButton_4_shezhi.setObjectName("pushButton_4_shezhi")
        self.gridLayout.addWidget(self.pushButton_4_shezhi, 0, 5, 1, 1)
        self.pushButton_2_xiazai = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_xiazai.setStyleSheet("background-color:rgb(15, 128, 255);color:rgb(255, 255, 255);border:1px groove gray;border-radius:10px;padding:2px 9px;border-style: outset;")
        self.pushButton_2_xiazai.setObjectName("pushButton_2_xiazai")
        self.gridLayout.addWidget(self.pushButton_2_xiazai, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.pushButton_3_lianji = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3_lianji.setStyleSheet("background-color:rgb(15, 128, 255);color:rgb(255, 255, 255);border:1px groove gray;border-radius:10px;padding:2px 9px;border-style: outset;")
        self.pushButton_3_lianji.setObjectName("pushButton_3_lianji")
        self.gridLayout.addWidget(self.pushButton_3_lianji, 0, 4, 1, 1)
        self.stackedWidget_zhu = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_zhu.setStyleSheet("background-color:rgb(102, 204, 255)")
        self.stackedWidget_zhu.setObjectName("stackedWidget_zhu")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_home)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_user_xuanze = QtWidgets.QComboBox(self.page_home)
        self.comboBox_user_xuanze.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_user_xuanze.setObjectName("comboBox_user_xuanze")
        self.gridLayout_2.addWidget(self.comboBox_user_xuanze, 3, 2, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 5, 2, 1, 3)
        self.pushButton_start_game = QtWidgets.QPushButton(self.page_home)
        self.pushButton_start_game.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_start_game.setObjectName("pushButton_start_game")
        self.gridLayout_2.addWidget(self.pushButton_start_game, 6, 2, 1, 3)
        self.pushButton_login_Mcjang = QtWidgets.QPushButton(self.page_home)
        self.pushButton_login_Mcjang.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_login_Mcjang.setObjectName("pushButton_login_Mcjang")
        self.gridLayout_2.addWidget(self.pushButton_login_Mcjang, 1, 3, 1, 1)
        self.stackedWidget_Login = QtWidgets.QStackedWidget(self.page_home)
        self.stackedWidget_Login.setObjectName("stackedWidget_Login")
        self.page_home_login_weiruan = QtWidgets.QWidget()
        self.page_home_login_weiruan.setObjectName("page_home_login_weiruan")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_home_login_weiruan)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_home_login_weiruan)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_5.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.page_home_login_weiruan)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.page_home_login_weiruan)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_5.addWidget(self.pushButton_12, 2, 0, 1, 1)
        self.stackedWidget_Login.addWidget(self.page_home_login_weiruan)
        self.page_home_login_Mcjang = QtWidgets.QWidget()
        self.page_home_login_Mcjang.setObjectName("page_home_login_Mcjang")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_home_login_Mcjang)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_home_login_Mcjang)
        self.lineEdit_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_6.addWidget(self.lineEdit_4, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_home_login_Mcjang)
        self.lineEdit_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_6.addWidget(self.lineEdit_3, 0, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.page_home_login_Mcjang)
        self.pushButton_13.setStyleSheet("color:rgb(255, 255, 255)")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_6.addWidget(self.pushButton_13, 2, 0, 1, 1)
        self.stackedWidget_Login.addWidget(self.page_home_login_Mcjang)
        self.page_home_login_lixian = QtWidgets.QWidget()
        self.page_home_login_lixian.setObjectName("page_home_login_lixian")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_home_login_lixian)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_home_login_lixian)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_9.addWidget(self.lineEdit_5, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.page_home_login_lixian)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_9.addWidget(self.pushButton, 1, 0, 1, 1)
        self.stackedWidget_Login.addWidget(self.page_home_login_lixian)
        self.page_home_login_starting = QtWidgets.QWidget()
        self.page_home_login_starting.setObjectName("page_home_login_starting")
        self.stackedWidget_Login.addWidget(self.page_home_login_starting)
        self.gridLayout_2.addWidget(self.stackedWidget_Login, 2, 2, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 3)
        self.stackedWidget_tongzhi = QtWidgets.QStackedWidget(self.page_home)
        self.stackedWidget_tongzhi.setStyleSheet("")
        self.stackedWidget_tongzhi.setObjectName("stackedWidget_tongzhi")
        self.page_tongzhi = QtWidgets.QWidget()
        self.page_tongzhi.setObjectName("page_tongzhi")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_tongzhi)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_tongzhi)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_8.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.stackedWidget_tongzhi.addWidget(self.page_tongzhi)
        self.page_tongzhi_ing = QtWidgets.QWidget()
        self.page_tongzhi_ing.setObjectName("page_tongzhi_ing")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_tongzhi_ing)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem4, 8, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 9, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem6, 7, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_tongzhi_ing)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 4, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.page_tongzhi_ing)
        self.progressBar.setStyleSheet("color:rgb(255, 255, 255)")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_7.addWidget(self.progressBar, 6, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem7, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem8, 10, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem9, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem10, 5, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem11, 6, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem12, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem13, 3, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem14, 6, 2, 1, 1)
        self.stackedWidget_tongzhi.addWidget(self.page_tongzhi_ing)
        self.gridLayout_2.addWidget(self.stackedWidget_tongzhi, 0, 5, 8, 1)
        self.pushButton_login_weiruan = QtWidgets.QPushButton(self.page_home)
        self.pushButton_login_weiruan.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_login_weiruan.setObjectName("pushButton_login_weiruan")
        self.gridLayout_2.addWidget(self.pushButton_login_weiruan, 1, 2, 1, 1)
        self.pushButton_login_lixian = QtWidgets.QPushButton(self.page_home)
        self.pushButton_login_lixian.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_login_lixian.setObjectName("pushButton_login_lixian")
        self.gridLayout_2.addWidget(self.pushButton_login_lixian, 1, 4, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 7, 3, 1, 1)
        self.stackedWidget_zhu.addWidget(self.page_home)
        self.page_xiazai = QtWidgets.QWidget()
        self.page_xiazai.setObjectName("page_xiazai")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_xiazai)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_xiazai_mode = QtWidgets.QPushButton(self.page_xiazai)
        self.pushButton_xiazai_mode.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_xiazai_mode.setObjectName("pushButton_xiazai_mode")
        self.gridLayout_3.addWidget(self.pushButton_xiazai_mode, 2, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem16, 10, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem17, 9, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem18, 8, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem19, 1, 0, 1, 1)
        self.pushButton_xiazai_zhenghebao = QtWidgets.QPushButton(self.page_xiazai)
        self.pushButton_xiazai_zhenghebao.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_xiazai_zhenghebao.setObjectName("pushButton_xiazai_zhenghebao")
        self.gridLayout_3.addWidget(self.pushButton_xiazai_zhenghebao, 4, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem20, 7, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem21, 5, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem22, 3, 0, 1, 1)
        self.pushButton_xiazai_game = QtWidgets.QPushButton(self.page_xiazai)
        self.pushButton_xiazai_game.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_xiazai_game.setObjectName("pushButton_xiazai_game")
        self.gridLayout_3.addWidget(self.pushButton_xiazai_game, 0, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem23, 6, 0, 1, 1)
        self.stackedWidget_xiazai_game = QtWidgets.QStackedWidget(self.page_xiazai)
        self.stackedWidget_xiazai_game.setObjectName("stackedWidget_xiazai_game")
        self.page_xiazai_game = QtWidgets.QWidget()
        self.page_xiazai_game.setObjectName("page_xiazai_game")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_xiazai_game)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.page_xiazai_game)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_4.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.stackedWidget_xiazai_game.addWidget(self.page_xiazai_game)
        self.page_xiazai_mod = QtWidgets.QWidget()
        self.page_xiazai_mod.setObjectName("page_xiazai_mod")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_xiazai_mod)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_6 = QtWidgets.QLabel(self.page_xiazai_mod)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_12.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.page_xiazai_mod)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_12.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.page_xiazai_mod)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_12.addWidget(self.label_7, 2, 3, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.page_xiazai_mod)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_12.addWidget(self.comboBox_4, 4, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.page_xiazai_mod)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_12.addWidget(self.label_5, 0, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.page_xiazai_mod)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_12.addWidget(self.comboBox_2, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.page_xiazai_mod)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_12.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_xiazai_mod)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_12.addWidget(self.label_9, 4, 3, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.page_xiazai_mod)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_12.addWidget(self.comboBox_5, 4, 4, 1, 2)
        self.comboBox_3 = QtWidgets.QComboBox(self.page_xiazai_mod)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_12.addWidget(self.comboBox_3, 2, 4, 1, 2)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_xiazai_mod)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_12.addWidget(self.lineEdit_6, 0, 4, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.page_xiazai_mod)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_12.addWidget(self.comboBox, 0, 1, 1, 2)
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.page_xiazai_mod)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "1")
        self.gridLayout_12.addWidget(self.treeWidget_2, 6, 0, 1, 6)
        self.stackedWidget_xiazai_game.addWidget(self.page_xiazai_mod)
        self.gridLayout_3.addWidget(self.stackedWidget_xiazai_game, 0, 1, 11, 1)
        self.stackedWidget_zhu.addWidget(self.page_xiazai)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)
        self.stackedWidget_zhu.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.stackedWidget = QtWidgets.QStackedWidget(self.page_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.gridLayout_11.addWidget(self.stackedWidget, 0, 1, 10, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_11.addItem(spacerItem24, 6, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_11.addItem(spacerItem25, 8, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_11.addItem(spacerItem26, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_11.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_11.addWidget(self.pushButton_3, 2, 0, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_11.addItem(spacerItem27, 7, 0, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_11.addItem(spacerItem28, 4, 0, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_11.addItem(spacerItem29, 1, 0, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_11.addItem(spacerItem30, 3, 0, 1, 1)
        self.stackedWidget_zhu.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget_zhu.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stackedWidget_zhu, 1, 0, 1, 9)
        self.pushButton_0_chose = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0_chose.setStyleSheet("background-image: url(:/png/picture/close.png);\n"
"border-image: url(:/png/picture/close.png);\n"
"image: url(:/png/picture/close.png);\n"
"\n"
"")
        self.pushButton_0_chose.setText("")
        self.pushButton_0_chose.setObjectName("pushButton_0_chose")
        self.gridLayout.addWidget(self.pushButton_0_chose, 0, 8, 1, 1)
        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)
        self.stackedWidget_zhu.setCurrentIndex(1)
        self.stackedWidget_Login.setCurrentIndex(1)
        self.stackedWidget_tongzhi.setCurrentIndex(1)
        self.stackedWidget_xiazai_game.setCurrentIndex(1)
        self.pushButton_0_chose.clicked.connect(MOS.close)
        QtCore.QMetaObject.connectSlotsByName(MOS)
    def click_pushButton_1(self):  # 点击触发
        self.stackedWidget_zhu.setCurrentIndex(0)  # 打开 stackedWidget > page_0

    def click_pushButton_2(self):  # 点击触发
        self.stackedWidget_zhu.setCurrentIndex(1)  # 打开 stackedWidget > page_0

    def click_pushButton_3(self):  # 点击触发
        self.stackedWidget_zhu.setCurrentIndex(2)  # 打开 stackedWidget > page_0

    def click_pushButton_4(self):  # 点击触发
        self.stackedWidget_zhu.setCurrentIndex(3)  # 打开 stackedWidget > page_0

    def click_pushButton_5(self):  # 点击触发
        self.stackedWidget_zhu.setCurrentIndex(4)  # 打开 stackedWidget > page_0

    def click_pushButton_login_weiruan(self):
        self.stackedWidget_Login.setCurrentIndex(0)

    def click_pushButton_login_Mcjang(self):
        self.stackedWidget_Login.setCurrentIndex(1)

    def click_pushButton_login_lixian(self):
        self.stackedWidget_Login.setCurrentIndex(2)

    def retranslateUi(self, MOS):
        _translate = QtCore.QCoreApplication.translate
        MOS.setWindowTitle(_translate("MOS", "MainWindow"))
        self.label_3.setText(_translate("MOS", "MOS 1"))
        self.pushButton_1_home.setText(_translate("MOS", "主页"))
        self.pushButton_5_about.setText(_translate("MOS", "关于"))
        self.pushButton_4_shezhi.setText(_translate("MOS", "设置"))
        self.pushButton_2_xiazai.setText(_translate("MOS", "下载"))
        self.pushButton_3_lianji.setText(_translate("MOS", "联机"))
        self.pushButton_start_game.setText(_translate("MOS", "启动！"))
        self.pushButton_login_Mcjang.setText(_translate("MOS", "Mcjang登陆"))
        self.lineEdit_2.setPlaceholderText(_translate("MOS", "密码"))
        self.lineEdit.setPlaceholderText(_translate("MOS", "用户名"))
        self.pushButton_12.setText(_translate("MOS", "登陆"))
        self.lineEdit_4.setPlaceholderText(_translate("MOS", "密码"))
        self.lineEdit_3.setPlaceholderText(_translate("MOS", "用户名"))
        self.pushButton_13.setText(_translate("MOS", "登陆"))
        self.lineEdit_5.setPlaceholderText(_translate("MOS", "用户名"))
        self.pushButton.setText(_translate("MOS", "登陆"))
        self.label_2.setText(_translate("MOS", "公告正在加载中。。。请稍后。。。"))
        self.pushButton_login_weiruan.setText(_translate("MOS", "微软登陆"))
        self.pushButton_login_lixian.setText(_translate("MOS", "离线登录"))
        self.pushButton_xiazai_mode.setText(_translate("MOS", "Mod"))
        self.pushButton_xiazai_zhenghebao.setText(_translate("MOS", "整合包"))
        self.pushButton_xiazai_game.setText(_translate("MOS", "游戏"))
        self.treeWidget.headerItem().setText(0, _translate("MOS", "游戏版本"))
        self.treeWidget.headerItem().setText(1, _translate("MOS", "说明"))
        self.label_6.setText(_translate("MOS", "下载源"))
        self.label_8.setText(_translate("MOS", "类别"))
        self.label_7.setText(_translate("MOS", "排序方式"))
        self.label_5.setText(_translate("MOS", "搜索"))
        self.label_4.setText(_translate("MOS", "下载到:"))
        self.label_9.setText(_translate("MOS", "游戏版本"))
        self.lineEdit_6.setPlaceholderText(_translate("MOS", "支持中文搜索"))
        self.label.setText(_translate("MOS", "还没有开发好啦"))
        self.pushButton_2.setText(_translate("MOS", "启动器设置"))
        self.pushButton_3.setText(_translate("MOS", "游戏全局设置"))
        self.pushButton_1_home.clicked.connect(self.click_pushButton_1)  # 点击 pushButton_1_home 触发
        self.pushButton_2_xiazai.clicked.connect(self.click_pushButton_2)  # 点击 pushButton_2 触发
        self.pushButton_3_lianji.clicked.connect(self.click_pushButton_3)  # 点击 pushButton_3 触发
        self.pushButton_4_shezhi.clicked.connect(self.click_pushButton_4)  # 点击 pushButton_4 触发
        self.pushButton_5_about.clicked.connect(self.click_pushButton_5)  # 点击 pushButton_5 触发
        self.pushButton_login_weiruan.clicked.connect(self.click_pushButton_login_weiruan)
        self.pushButton_login_Mcjang.clicked.connect(self.click_pushButton_login_Mcjang)
        self.pushButton_login_lixian.clicked.connect(self.click_pushButton_login_lixian)

if __name__ == '__main__':
    print ("程序已开始运行！")
    app = QtWidgets.QApplication(sys.argv)
    print ("请稍等...")
    MainWindow = QtWidgets.QMainWindow()
    print ("创建窗口对象成功！")
    ui = Ui_MOS()
    print ("创建PyQt窗口对象成功！")
    ui.setupUi(MainWindow)
    print ("初始化设置成功！")
    MainWindow.show()
    print ("已成功显示窗体")
    sys.exit(app.exec())