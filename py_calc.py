from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QShortcut


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 800))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/calculate_FILL0_wght400_GRAD0_opsz48.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    color: white;\n"
                                 "    background-color: #121212;\n"
                                 "    font-family: SF Pro Display;\n"
                                 "    font-size: 16pt;\n"
                                 "    font-weight: 600;\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "    background-color: #888;\n"
                                 "    border-radius: 25px;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #ababab;\n"
                                 "    border-radius: 25px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #ababab;\n"
                                 "    border-radius: 25px;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setToolTipDuration(-4)
        self.label.setStyleSheet("color:#888")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("font-size:40px;\n"
                                    "border: none;")
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lay_btn = QtWidgets.QGridLayout()
        self.lay_btn.setObjectName("lay_btn")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_6.setStyleSheet("")
        self.btn_6.setObjectName("btn_6")
        self.lay_btn.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_div.setFont(font)
        self.btn_div.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_div.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_div.setStyleSheet("QPushButton {\n"
                                   "    background-color: #eba352;\n"
                                   "    border: none;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: #dbb284;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: #fafafa;\n"
                                   "    color: #eba352\n"
                                   "}")
        self.btn_div.setObjectName("btn_div")
        self.lay_btn.addWidget(self.btn_div, 0, 3, 1, 1)
        self.btn_backspace = QtWidgets.QPushButton(self.centralwidget)
        self.btn_backspace.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_backspace.setFont(font)
        self.btn_backspace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_backspace.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_backspace.setStyleSheet("QPushButton {\n"
                                         "    background-color: #e5e5e5;\n"
                                         "    border: none;\n"
                                         "    color:black;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #fafafa;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: #fafafa;\n"
                                         "}")
        self.btn_backspace.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/backspace_FILL0_wght400_GRAD0_opsz48.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btn_backspace.setIcon(icon1)
        self.btn_backspace.setIconSize(QtCore.QSize(30, 30))
        self.btn_backspace.setObjectName("btn_backspace")
        self.lay_btn.addWidget(self.btn_backspace, 0, 1, 1, 1)
        self.btn_min_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_min_add.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_min_add.sizePolicy().hasHeightForWidth())
        self.btn_min_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_min_add.setFont(font)
        self.btn_min_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_min_add.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_min_add.setStyleSheet("QPushButton {\n"
                                        "    background-color: #e5e5e5;\n"
                                        "    border: none;\n"
                                        "    color:black;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #fafafa;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #fafafa;\n"
                                        "}")
        self.btn_min_add.setObjectName("btn_min_plus")
        self.lay_btn.addWidget(self.btn_min_add, 0, 2, 1, 1)
        self.btn_c = QtWidgets.QPushButton(self.centralwidget)
        self.btn_c.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_c.setFont(font)
        self.btn_c.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_c.setStyleSheet("QPushButton {\n"
                                 "    background-color: #e5e5e5;\n"
                                 "    border: none;\n"
                                 "    color:black;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #fafafa;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #fafafa;\n"
                                 "}")
        self.btn_c.setObjectName("btn_c")
        self.lay_btn.addWidget(self.btn_c, 0, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_1.setStyleSheet("")
        self.btn_1.setObjectName("btn_1")
        self.lay_btn.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_2.setStyleSheet("")
        self.btn_2.setObjectName("btn_2")
        self.lay_btn.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_3.setStyleSheet("")
        self.btn_3.setObjectName("btn_3")
        self.lay_btn.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        self.btn_point.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_point.setFont(font)
        self.btn_point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_point.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_point.setStyleSheet("")
        self.btn_point.setObjectName("btn_point")
        self.lay_btn.addWidget(self.btn_point, 4, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_0.setTabletTracking(False)
        self.btn_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_0.setStyleSheet("text-align: left;\n"
                                 "padding: 10px 10px 10px 30px;")
        self.btn_0.setObjectName("btn_0")
        self.lay_btn.addWidget(self.btn_0, 4, 0, 1, 2)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_add.setStyleSheet("QPushButton {\n"
                                    "    background-color: #eba352;\n"
                                    "    border: none;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: #dbb284;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: #fafafa;\n"
                                    "    color: #eba352\n"
                                    "}")
        self.btn_add.setObjectName("btn_plus")
        self.lay_btn.addWidget(self.btn_add, 3, 3, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_equal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_equal.setStyleSheet("QPushButton {\n"
                                     "    background-color: #eba352;\n"
                                     "    border: none;\n"
                                     "\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #dbb284;\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: #dbb284;\n"
                                     "\n"
                                     "}")
        self.btn_equal.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/равно.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_equal.setIcon(icon2)

        for sc in ('=', 'Enter', 'Return'):
            QShortcut(sc, self.btn_equal).activated.connect(self.btn_equal.animateClick)

        self.btn_equal.setObjectName("btn_equal")
        self.lay_btn.addWidget(self.btn_equal, 4, 3, 1, 1)
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mul.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mul.setFont(font)
        self.btn_mul.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_mul.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_mul.setStyleSheet("QPushButton {\n"
                                   "    background-color: #eba352;\n"
                                   "    border: none;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: #dbb284;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: #fafafa;\n"
                                   "    color: #eba352\n"
                                   "}")
        self.btn_mul.setObjectName("btn_mul")
        for sc in '*':
            QShortcut(sc, self.btn_mul).activated.connect(self.btn_mul.animateClick)
        self.lay_btn.addWidget(self.btn_mul, 1, 3, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_7.setStyleSheet("")
        self.btn_7.setObjectName("btn_7")
        self.lay_btn.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_5.setStyleSheet("")
        self.btn_5.setObjectName("btn_5")
        self.lay_btn.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_9.setStyleSheet("")
        self.btn_9.setObjectName("btn_9")
        self.lay_btn.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_8.setStyleSheet("")
        self.btn_8.setObjectName("btn_8")
        self.lay_btn.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_4.setStyleSheet("")
        self.btn_4.setObjectName("btn_4")
        self.lay_btn.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_minus.setStyleSheet("QPushButton {\n"
                                     "    background-color: #eba352;\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #dbb284;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: #fafafa;\n"
                                     "    color: #eba352;\n"
                                     "    \n"
                                     "}")
        self.btn_minus.setObjectName("btn_minus")
        self.lay_btn.addWidget(self.btn_minus, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.lay_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_6.setShortcut(_translate("MainWindow", "6"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_div.setShortcut(_translate("MainWindow", "/"))
        self.btn_backspace.setShortcut(_translate("MainWindow", "Backspace"))
        self.btn_min_add.setText(_translate("MainWindow", "+-"))
        self.btn_c.setText(_translate("MainWindow", "С"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_1.setShortcut(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_2.setShortcut(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_3.setShortcut(_translate("MainWindow", "3"))
        self.btn_point.setText(_translate("MainWindow", "."))

        for sc in (',', '.'):
            QShortcut(sc, self.btn_point).activated.connect(self.btn_point.animateClick)

        self.btn_0.setWhatsThis(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" "
                                           "font-style:italic;\">565</span></p></body></html>"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_0.setShortcut(_translate("MainWindow", "0"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_add.setShortcut(_translate("MainWindow", "+"))
        self.btn_mul.setText(_translate("MainWindow", "×"))
        self.btn_mul.setShortcut(_translate("MainWindow", "×"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_7.setShortcut(_translate("MainWindow", "7"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_5.setShortcut(_translate("MainWindow", "5"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_9.setShortcut(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_8.setShortcut(_translate("MainWindow", "8"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_4.setShortcut(_translate("MainWindow", "4"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_minus.setShortcut(_translate("MainWindow", "-"))


import files_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
