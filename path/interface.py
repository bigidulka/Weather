# Form implementation generated from reading ui file '.\interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 665)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("#MainWindow {\n"
"background-image: url(:/fons/fons/stock-photo-beautiful-light-blue-sky-clouds.jpg);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: transparent;\n"
"border: 2px solid transparent;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QFrame {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#nameCityCountry,#condition,#prognozDn, #prognoz14, #temp {\n"
"font-family: \"Verdana\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"border: 2px solid transparent;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 0.7);\n"
"border: 2px solid transparent\n"
"}\n"
"\n"
"#hourly_forecast,  #daily_forecast {\n"
"border-radius: 5px;\n"
"background-color:  rgba(255, 255, 255, 0.7);\n"
"padding: 5px;\n"
"}\n"
"\n"
"#hourly_forecast:hover,  #daily_forecast:hover {\n"
"border: 2px solid rgba(232, 232, 232, 0.7);\n"
"}\n"
"\n"
"\n"
"/*скролл арея*/\n"
"QScrollArea {\n"
"background-color: transparent;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#daily_scrollAreaCont, #hourly_scrollAreaCont {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*скроллбары*/\n"
"QScrollArea QFrame {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"background-color: transparent;\n"
"height: 10px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"background-color: rgba(255, 255, 255, 0.7);\n"
"border-radius: 5px;\n"
"border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:hover, QScrollBar::handle:pressed {\n"
"background-color: rgba(255, 255, 255, 0.9);\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"background-color: transparent;\n"
"width: 0px;\n"
"height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"border-right: 1px solid #fff;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"border-left: 1px solid #fff;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"min-width: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"/*поиск*/\n"
"#searhPanel {\n"
"background-color: rgba(255, 255, 255, 0.7);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"#searhPanel:hover {\n"
"border: 2px solid rgba(232, 232, 232, 0.7);\n"
"}\n"
"\n"
"\n"
"\n"
"#searchEdit {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QFrame(self.centralwidget)
        self.title.setMinimumSize(QtCore.QSize(0, 0))
        self.title.setMaximumSize(QtCore.QSize(16777215, 40))
        self.title.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.title.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title.setObjectName("title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_location = QtWidgets.QPushButton(self.title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_location.sizePolicy().hasHeightForWidth())
        self.search_location.setSizePolicy(sizePolicy)
        self.search_location.setMinimumSize(QtCore.QSize(50, 40))
        self.search_location.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/near_me_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_location.setIcon(icon)
        self.search_location.setObjectName("search_location")
        self.horizontalLayout.addWidget(self.search_location)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.hideBtn = QtWidgets.QPushButton(self.title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hideBtn.sizePolicy().hasHeightForWidth())
        self.hideBtn.setSizePolicy(sizePolicy)
        self.hideBtn.setMinimumSize(QtCore.QSize(50, 40))
        self.hideBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/remove_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.hideBtn.setIcon(icon1)
        self.hideBtn.setObjectName("hideBtn")
        self.horizontalLayout.addWidget(self.hideBtn)
        self.closeBtn = QtWidgets.QPushButton(self.title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMinimumSize(QtCore.QSize(50, 40))
        self.closeBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/close_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn)
        self.verticalLayout.addWidget(self.title)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout_2.setContentsMargins(4, 20, 4, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main = QtWidgets.QWidget(self.content)
        self.main.setStyleSheet("")
        self.main.setObjectName("main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.today = QtWidgets.QWidget(self.main)
        self.today.setStyleSheet("")
        self.today.setObjectName("today")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.today)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.basicInfo = QtWidgets.QFrame(self.today)
        self.basicInfo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.basicInfo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.basicInfo.setObjectName("basicInfo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.basicInfo)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.basicInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.nameCityCountry = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameCityCountry.sizePolicy().hasHeightForWidth())
        self.nameCityCountry.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        self.nameCityCountry.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nameCityCountry.setFont(font)
        self.nameCityCountry.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.nameCityCountry.setScaledContents(False)
        self.nameCityCountry.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.nameCityCountry.setObjectName("nameCityCountry")
        self.verticalLayout_5.addWidget(self.nameCityCountry)
        self.time = QtWidgets.QLabel(self.frame_2)
        palette = QtGui.QPalette()
        self.time.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.time.setFont(font)
        self.time.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.time.setObjectName("time")
        self.verticalLayout_5.addWidget(self.time)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.basicInfo)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 20, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ico = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ico.sizePolicy().hasHeightForWidth())
        self.ico.setSizePolicy(sizePolicy)
        self.ico.setText("")
        self.ico.setPixmap(QtGui.QPixmap(":/weatherDay/weather/64x64/day/113.png"))
        self.ico.setScaledContents(False)
        self.ico.setOpenExternalLinks(False)
        self.ico.setObjectName("ico")
        self.horizontalLayout_3.addWidget(self.ico)
        self.temp = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp.sizePolicy().hasHeightForWidth())
        self.temp.setSizePolicy(sizePolicy)
        self.temp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        self.temp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.temp.setFont(font)
        self.temp.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.temp.setObjectName("temp")
        self.horizontalLayout_3.addWidget(self.temp)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 5, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.condition = QtWidgets.QLabel(self.frame_5)
        palette = QtGui.QPalette()
        self.condition.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.condition.setFont(font)
        self.condition.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.condition.setObjectName("condition")
        self.verticalLayout_6.addWidget(self.condition)
        self.feels_like = QtWidgets.QLabel(self.frame_5)
        palette = QtGui.QPalette()
        self.feels_like.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.feels_like.setFont(font)
        self.feels_like.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.feels_like.setObjectName("feels_like")
        self.verticalLayout_6.addWidget(self.feels_like)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(self.basicInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.frame)
        self.verticalLayout_7.addWidget(self.basicInfo)
        self.verticalLayout_3.addWidget(self.today)
        self.hourly_forecast = QtWidgets.QWidget(self.main)
        self.hourly_forecast.setObjectName("hourly_forecast")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.hourly_forecast)
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.prognozDn = QtWidgets.QLabel(self.hourly_forecast)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prognozDn.sizePolicy().hasHeightForWidth())
        self.prognozDn.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        self.prognozDn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.prognozDn.setFont(font)
        self.prognozDn.setObjectName("prognozDn")
        self.verticalLayout_9.addWidget(self.prognozDn)
        self.hourly_scrollArea = QtWidgets.QScrollArea(self.hourly_forecast)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hourly_scrollArea.sizePolicy().hasHeightForWidth())
        self.hourly_scrollArea.setSizePolicy(sizePolicy)
        self.hourly_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.hourly_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.hourly_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.hourly_scrollArea.setWidgetResizable(True)
        self.hourly_scrollArea.setObjectName("hourly_scrollArea")
        self.hourly_scrollAreaCont = QtWidgets.QWidget()
        self.hourly_scrollAreaCont.setGeometry(QtCore.QRect(0, 0, 470, 123))
        self.hourly_scrollAreaCont.setStyleSheet("")
        self.hourly_scrollAreaCont.setObjectName("hourly_scrollAreaCont")
        self.hourly_scrollArea.setWidget(self.hourly_scrollAreaCont)
        self.verticalLayout_9.addWidget(self.hourly_scrollArea)
        self.verticalLayout_3.addWidget(self.hourly_forecast)
        self.daily_forecast = QtWidgets.QWidget(self.main)
        self.daily_forecast.setObjectName("daily_forecast")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.daily_forecast)
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.prognoz14 = QtWidgets.QLabel(self.daily_forecast)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prognoz14.sizePolicy().hasHeightForWidth())
        self.prognoz14.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        self.prognoz14.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.prognoz14.setFont(font)
        self.prognoz14.setObjectName("prognoz14")
        self.verticalLayout_8.addWidget(self.prognoz14)
        self.daily_scrollArea = QtWidgets.QScrollArea(self.daily_forecast)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daily_scrollArea.sizePolicy().hasHeightForWidth())
        self.daily_scrollArea.setSizePolicy(sizePolicy)
        self.daily_scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.daily_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.daily_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.daily_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.daily_scrollArea.setWidgetResizable(True)
        self.daily_scrollArea.setObjectName("daily_scrollArea")
        self.daily_scrollAreaCont = QtWidgets.QWidget()
        self.daily_scrollAreaCont.setGeometry(QtCore.QRect(0, 0, 474, 125))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daily_scrollAreaCont.sizePolicy().hasHeightForWidth())
        self.daily_scrollAreaCont.setSizePolicy(sizePolicy)
        self.daily_scrollAreaCont.setStyleSheet("")
        self.daily_scrollAreaCont.setObjectName("daily_scrollAreaCont")
        self.daily_scrollArea.setWidget(self.daily_scrollAreaCont)
        self.verticalLayout_8.addWidget(self.daily_scrollArea)
        self.verticalLayout_3.addWidget(self.daily_forecast)
        self.verticalLayout_2.addWidget(self.main)
        self.searhPanel = QtWidgets.QFrame(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searhPanel.sizePolicy().hasHeightForWidth())
        self.searhPanel.setSizePolicy(sizePolicy)
        self.searhPanel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.searhPanel.setStyleSheet("")
        self.searhPanel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.searhPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.searhPanel.setObjectName("searhPanel")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.searhPanel)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchEdit = QtWidgets.QPlainTextEdit(self.searhPanel)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchEdit.setFont(font)
        self.searchEdit.setUndoRedoEnabled(False)
        self.searchEdit.setPlainText("")
        self.searchEdit.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextEditable|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_2.addWidget(self.searchEdit)
        self.clear = QtWidgets.QPushButton(self.searhPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        self.clear.setMinimumSize(QtCore.QSize(30, 30))
        self.clear.setText("")
        self.clear.setIcon(icon2)
        self.clear.setObjectName("clear")
        self.horizontalLayout_2.addWidget(self.clear)
        self.search = QtWidgets.QPushButton(self.searhPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        self.search.setMinimumSize(QtCore.QSize(30, 30))
        self.search.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/search_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search.setIcon(icon3)
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.verticalLayout_2.addWidget(self.searhPanel)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameCityCountry.setText(_translate("MainWindow", "Микрорайон Завода 1 Мая, Киров"))
        self.time.setText(_translate("MainWindow", "Сейчас 12:53. Вчера в это время 6"))
        self.temp.setText(_translate("MainWindow", "6°"))
        self.condition.setText(_translate("MainWindow", "Пасмурно"))
        self.feels_like.setText(_translate("MainWindow", "Ощущается как +1"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.prognozDn.setText(_translate("MainWindow", "Почасовой прогноз"))
        self.prognoz14.setText(_translate("MainWindow", "Прогноз на 14 дней"))
