# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(606, 631)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"background-color: transparent;\n"
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
"#searhPanel:hover {\n"
"border: 1px solid rgba(200, 200, 200, 0.1);\n"
"}\n"
"\n"
"/*\u0438\u0437\u043c\u0435\u043d\u044f\u0435\u043c\u043e*/\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 0.7);\n"
"}\n"
"\n"
"#hourly_forecast,  #daily_forecast, #searhPanel {\n"
"border-radius: 5px;\n"
"background-color:  rgba(255, 255, 255, 0.7);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 3px;\n"
"border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:hover, QScrollBar::handle:pressed {\n"
"background-color: rgba(255, 255, 255, 0.7);\n"
"}\n"
"\n"
"\n"
"/*\u0441\u043a\u0440\u043e\u043b\u043b \u0430"
                        "\u0440\u0435\u044f*/\n"
"QScrollArea {\n"
"background-color: transparent;\n"
"border: none;\n"
"}\n"
"\n"
"#daily_scrollAreaCont, #hourly_scrollAreaCont {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*\u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u044b*/\n"
"QScrollArea QFrame {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"background-color: transparent;\n"
"height: 8px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"background-color: transparent;\n"
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
"/*\u043f\u043e\u0438\u0441\u043a*/\n"
"#searchEdit {\n"
"backgrou"
                        "nd-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QFrame(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 0))
        self.title.setMaximumSize(QSize(16777215, 40))
        self.title.setFrameShape(QFrame.NoFrame)
        self.title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.search_location = QPushButton(self.title)
        self.search_location.setObjectName(u"search_location")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_location.sizePolicy().hasHeightForWidth())
        self.search_location.setSizePolicy(sizePolicy)
        self.search_location.setMinimumSize(QSize(50, 40))
        self.search_location.setMaximumSize(QSize(12441234, 1241234))
        icon = QIcon()
        icon.addFile(u":/icons/icons/near_me_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_location.setIcon(icon)

        self.horizontalLayout.addWidget(self.search_location)

        self.error = QLabel(self.title)
        self.error.setObjectName(u"error")
        sizePolicy.setHeightForWidth(self.error.sizePolicy().hasHeightForWidth())
        self.error.setSizePolicy(sizePolicy)
        self.error.setMinimumSize(QSize(410, 0))
        self.error.setMaximumSize(QSize(410, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Montserrat SemiBold"])
        font1.setPointSize(8)
        self.error.setFont(font1)
        self.error.setWordWrap(True)

        self.horizontalLayout.addWidget(self.error)

        self.languageButton = QPushButton(self.title)
        self.languageButton.setObjectName(u"languageButton")

        self.horizontalLayout.addWidget(self.languageButton)

        self.hideBtn = QPushButton(self.title)
        self.hideBtn.setObjectName(u"hideBtn")
        sizePolicy.setHeightForWidth(self.hideBtn.sizePolicy().hasHeightForWidth())
        self.hideBtn.setSizePolicy(sizePolicy)
        self.hideBtn.setMinimumSize(QSize(50, 40))
        self.hideBtn.setMaximumSize(QSize(2141234, 12433124))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/remove_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hideBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.hideBtn)

        self.closeBtn = QPushButton(self.title)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMinimumSize(QSize(50, 40))
        self.closeBtn.setMaximumSize(QSize(1423123, 14124241))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/close_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.closeBtn)


        self.verticalLayout.addWidget(self.title)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 10, 4, 4)
        self.main = QWidget(self.content)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.main)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.today = QWidget(self.main)
        self.today.setObjectName(u"today")
        sizePolicy.setHeightForWidth(self.today.sizePolicy().hasHeightForWidth())
        self.today.setSizePolicy(sizePolicy)
        self.today.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.today)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.basicInfo = QFrame(self.today)
        self.basicInfo.setObjectName(u"basicInfo")
        self.basicInfo.setFrameShape(QFrame.StyledPanel)
        self.basicInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.basicInfo)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.basicInfo)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 0, 0, 0)
        self.nameCityCountry = QLabel(self.frame_2)
        self.nameCityCountry.setObjectName(u"nameCityCountry")
        sizePolicy.setHeightForWidth(self.nameCityCountry.sizePolicy().hasHeightForWidth())
        self.nameCityCountry.setSizePolicy(sizePolicy)
        palette = QPalette()
        self.nameCityCountry.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.nameCityCountry.setFont(font2)
        self.nameCityCountry.setTextFormat(Qt.AutoText)
        self.nameCityCountry.setScaledContents(False)
        self.nameCityCountry.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.nameCityCountry.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.nameCityCountry)

        self.time = QLabel(self.frame_2)
        self.time.setObjectName(u"time")
        sizePolicy.setHeightForWidth(self.time.sizePolicy().hasHeightForWidth())
        self.time.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        self.time.setPalette(palette1)
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(12)
        self.time.setFont(font3)
        self.time.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.time)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.basicInfo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ico = QLabel(self.frame_3)
        self.ico.setObjectName(u"ico")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ico.sizePolicy().hasHeightForWidth())
        self.ico.setSizePolicy(sizePolicy1)
        self.ico.setPixmap(QPixmap(u":/weatherDay/weather/64x64/day/113.png"))
        self.ico.setScaledContents(False)
        self.ico.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ico.setMargin(0)
        self.ico.setOpenExternalLinks(False)

        self.horizontalLayout_3.addWidget(self.ico)

        self.temp = QLabel(self.frame_3)
        self.temp.setObjectName(u"temp")
        sizePolicy.setHeightForWidth(self.temp.sizePolicy().hasHeightForWidth())
        self.temp.setSizePolicy(sizePolicy)
        self.temp.setMaximumSize(QSize(16777215, 16777215))
        palette2 = QPalette()
        self.temp.setPalette(palette2)
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(40)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.temp.setFont(font4)
        self.temp.setTextFormat(Qt.AutoText)

        self.horizontalLayout_3.addWidget(self.temp)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 5, 0)
        self.condition = QLabel(self.frame_5)
        self.condition.setObjectName(u"condition")
        palette3 = QPalette()
        self.condition.setPalette(palette3)
        self.condition.setFont(font2)
        self.condition.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.condition.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.condition)

        self.feels_like = QLabel(self.frame_5)
        self.feels_like.setObjectName(u"feels_like")
        palette4 = QPalette()
        self.feels_like.setPalette(palette4)
        self.feels_like.setFont(font3)
        self.feels_like.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.feels_like.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.feels_like)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame = QFrame(self.basicInfo)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        font5 = QFont()
        font5.setPointSize(12)
        self.frame.setFont(font5)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.windIco = QLabel(self.frame)
        self.windIco.setObjectName(u"windIco")
        sizePolicy.setHeightForWidth(self.windIco.sizePolicy().hasHeightForWidth())
        self.windIco.setSizePolicy(sizePolicy)
        self.windIco.setMaximumSize(QSize(30, 30))
        self.windIco.setBaseSize(QSize(0, 0))
        self.windIco.setPixmap(QPixmap(u":/icons/icons/air_FILL0_wght400_GRAD0_opsz48.svg"))
        self.windIco.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.windIco)

        self.windText = QLabel(self.frame)
        self.windText.setObjectName(u"windText")
        sizePolicy.setHeightForWidth(self.windText.sizePolicy().hasHeightForWidth())
        self.windText.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamilies([u"Verdana"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.windText.setFont(font6)

        self.horizontalLayout_4.addWidget(self.windText)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.humIco = QLabel(self.frame)
        self.humIco.setObjectName(u"humIco")
        sizePolicy.setHeightForWidth(self.humIco.sizePolicy().hasHeightForWidth())
        self.humIco.setSizePolicy(sizePolicy)
        self.humIco.setMaximumSize(QSize(30, 30))
        self.humIco.setPixmap(QPixmap(u":/icons/icons/humidity_percentage_FILL0_wght400_GRAD0_opsz48.svg"))
        self.humIco.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.humIco)

        self.humText = QLabel(self.frame)
        self.humText.setObjectName(u"humText")
        sizePolicy.setHeightForWidth(self.humText.sizePolicy().hasHeightForWidth())
        self.humText.setSizePolicy(sizePolicy)
        self.humText.setFont(font6)

        self.horizontalLayout_4.addWidget(self.humText)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pressIco = QLabel(self.frame)
        self.pressIco.setObjectName(u"pressIco")
        sizePolicy.setHeightForWidth(self.pressIco.sizePolicy().hasHeightForWidth())
        self.pressIco.setSizePolicy(sizePolicy)
        self.pressIco.setMaximumSize(QSize(30, 30))
        self.pressIco.setPixmap(QPixmap(u":/icons/icons/compress_FILL0_wght400_GRAD0_opsz48.svg"))
        self.pressIco.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.pressIco)

        self.pressText = QLabel(self.frame)
        self.pressText.setObjectName(u"pressText")
        sizePolicy.setHeightForWidth(self.pressText.sizePolicy().hasHeightForWidth())
        self.pressText.setSizePolicy(sizePolicy)
        self.pressText.setFont(font6)

        self.horizontalLayout_4.addWidget(self.pressText)


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout_7.addWidget(self.basicInfo)


        self.verticalLayout_3.addWidget(self.today)

        self.hourly_forecast = QWidget(self.main)
        self.hourly_forecast.setObjectName(u"hourly_forecast")
        sizePolicy3.setHeightForWidth(self.hourly_forecast.sizePolicy().hasHeightForWidth())
        self.hourly_forecast.setSizePolicy(sizePolicy3)
        self.hourly_forecast.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.hourly_forecast)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(9, 6, 6, 3)
        self.prognozDn = QLabel(self.hourly_forecast)
        self.prognozDn.setObjectName(u"prognozDn")
        sizePolicy3.setHeightForWidth(self.prognozDn.sizePolicy().hasHeightForWidth())
        self.prognozDn.setSizePolicy(sizePolicy3)
        palette5 = QPalette()
        self.prognozDn.setPalette(palette5)
        font7 = QFont()
        font7.setFamilies([u"Verdana"])
        font7.setPointSize(9)
        font7.setBold(True)
        self.prognozDn.setFont(font7)

        self.verticalLayout_9.addWidget(self.prognozDn)

        self.hourly_scrollArea = QScrollArea(self.hourly_forecast)
        self.hourly_scrollArea.setObjectName(u"hourly_scrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.hourly_scrollArea.sizePolicy().hasHeightForWidth())
        self.hourly_scrollArea.setSizePolicy(sizePolicy4)
        self.hourly_scrollArea.setMinimumSize(QSize(0, 90))
        self.hourly_scrollArea.setBaseSize(QSize(0, 0))
        self.hourly_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.hourly_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.hourly_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.hourly_scrollArea.setWidgetResizable(True)
        self.hourly_scrollAreaCont = QWidget()
        self.hourly_scrollAreaCont.setObjectName(u"hourly_scrollAreaCont")
        self.hourly_scrollAreaCont.setGeometry(QRect(0, 0, 583, 90))
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.hourly_scrollAreaCont.sizePolicy().hasHeightForWidth())
        self.hourly_scrollAreaCont.setSizePolicy(sizePolicy5)
        self.hourly_scrollAreaCont.setStyleSheet(u"")
        self.hourly_scrollArea.setWidget(self.hourly_scrollAreaCont)

        self.verticalLayout_9.addWidget(self.hourly_scrollArea)


        self.verticalLayout_3.addWidget(self.hourly_forecast)

        self.daily_forecast = QWidget(self.main)
        self.daily_forecast.setObjectName(u"daily_forecast")
        sizePolicy3.setHeightForWidth(self.daily_forecast.sizePolicy().hasHeightForWidth())
        self.daily_forecast.setSizePolicy(sizePolicy3)
        self.verticalLayout_8 = QVBoxLayout(self.daily_forecast)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 6, 6, 3)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.calendar = QLabel(self.daily_forecast)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setMaximumSize(QSize(20, 20))
        self.calendar.setPixmap(QPixmap(u":/icons/icons/calendar_month_FILL0_wght400_GRAD0_opsz48.svg"))
        self.calendar.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.calendar)

        self.prognoz14 = QLabel(self.daily_forecast)
        self.prognoz14.setObjectName(u"prognoz14")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.prognoz14.sizePolicy().hasHeightForWidth())
        self.prognoz14.setSizePolicy(sizePolicy6)
        palette6 = QPalette()
        self.prognoz14.setPalette(palette6)
        self.prognoz14.setFont(font7)

        self.horizontalLayout_5.addWidget(self.prognoz14)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.daily_scrollArea = QScrollArea(self.daily_forecast)
        self.daily_scrollArea.setObjectName(u"daily_scrollArea")
        sizePolicy4.setHeightForWidth(self.daily_scrollArea.sizePolicy().hasHeightForWidth())
        self.daily_scrollArea.setSizePolicy(sizePolicy4)
        self.daily_scrollArea.setMinimumSize(QSize(0, 0))
        self.daily_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.daily_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.daily_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.daily_scrollArea.setWidgetResizable(True)
        self.daily_scrollAreaCont = QWidget()
        self.daily_scrollAreaCont.setObjectName(u"daily_scrollAreaCont")
        self.daily_scrollAreaCont.setGeometry(QRect(0, 0, 583, 42))
        sizePolicy5.setHeightForWidth(self.daily_scrollAreaCont.sizePolicy().hasHeightForWidth())
        self.daily_scrollAreaCont.setSizePolicy(sizePolicy5)
        self.daily_scrollAreaCont.setStyleSheet(u"")
        self.daily_scrollArea.setWidget(self.daily_scrollAreaCont)

        self.verticalLayout_8.addWidget(self.daily_scrollArea)


        self.verticalLayout_3.addWidget(self.daily_forecast)


        self.verticalLayout_2.addWidget(self.main)

        self.searhPanel = QFrame(self.content)
        self.searhPanel.setObjectName(u"searhPanel")
        sizePolicy.setHeightForWidth(self.searhPanel.sizePolicy().hasHeightForWidth())
        self.searhPanel.setSizePolicy(sizePolicy)
        self.searhPanel.setMaximumSize(QSize(16777215, 40))
        self.searhPanel.setStyleSheet(u"")
        self.searhPanel.setFrameShape(QFrame.StyledPanel)
        self.searhPanel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.searhPanel)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.searchEdit = QLineEdit(self.searhPanel)
        self.searchEdit.setObjectName(u"searchEdit")
        sizePolicy4.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy4)
        self.searchEdit.setMinimumSize(QSize(0, 28))
        self.searchEdit.setMaximumSize(QSize(16777215, 28))
        font8 = QFont()
        font8.setFamilies([u"Verdana"])
        font8.setPointSize(13)
        self.searchEdit.setFont(font8)
        self.searchEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.searchEdit)

        self.clear = QPushButton(self.searhPanel)
        self.clear.setObjectName(u"clear")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy7)
        self.clear.setMinimumSize(QSize(30, 30))
        self.clear.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.clear)

        self.search = QPushButton(self.searhPanel)
        self.search.setObjectName(u"search")
        sizePolicy7.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy7)
        self.search.setMinimumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/search_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.search)


        self.verticalLayout_2.addWidget(self.searhPanel)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.search_location.setText("")
        self.error.setText("")
        self.languageButton.setText(QCoreApplication.translate("MainWindow", u"language", None))
        self.hideBtn.setText("")
        self.closeBtn.setText("")
        self.nameCityCountry.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043a\u0440\u043e\u0440\u0430\u0439\u043e\u043d \u0417\u0430\u0432\u043e\u0434\u0430 1 \u041c\u0430\u044f, \u041a\u0438\u0440\u043e\u0432", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0439\u0447\u0430\u0441 12:53. \u0412\u0447\u0435\u0440\u0430 \u0432 \u044d\u0442\u043e \u0432\u0440\u0435\u043c\u044f 6", None))
        self.ico.setText("")
        self.temp.setText(QCoreApplication.translate("MainWindow", u"6\u00b0", None))
        self.condition.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u043c\u0443\u0440\u043d\u043e", None))
        self.feels_like.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0449\u0443\u0449\u0430\u0435\u0442\u0441\u044f \u043a\u0430\u043a +1", None))
        self.windIco.setText("")
        self.windText.setText(QCoreApplication.translate("MainWindow", u"1,0 \u043c/\u0441, \u042e\u0417", None))
        self.humIco.setText("")
        self.humText.setText(QCoreApplication.translate("MainWindow", u"30%", None))
        self.pressIco.setText("")
        self.pressText.setText(QCoreApplication.translate("MainWindow", u"751 \u043c\u043c \u0440\u0442. \u0441\u0442.", None))
        self.prognozDn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0430\u0441\u043e\u0432\u043e\u0439 \u043f\u0440\u043e\u0433\u043d\u043e\u0437", None))
        self.calendar.setText("")
        self.prognoz14.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437 \u043d\u0430 14 \u0434\u043d\u0435\u0439", None))
        self.clear.setText("")
        self.search.setText("")
    # retranslateUi

