# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'am_i_dot2TrckDx.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGridLayout,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1944, 894)
        icon = QIcon()
        icon.addFile(u"media/ma_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionWing_1 = QAction(MainWindow)
        self.actionWing_1.setObjectName(u"actionWing_1")
        self.actionWing_2 = QAction(MainWindow)
        self.actionWing_2.setObjectName(u"actionWing_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1944, 33))
        self.menuOpen_new_Wing_View = QMenu(self.menubar)
        self.menuOpen_new_Wing_View.setObjectName(u"menuOpen_new_Wing_View")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Wing1_dock = QDockWidget(MainWindow)
        self.Wing1_dock.setObjectName(u"Wing1_dock")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Wing1_dock.sizePolicy().hasHeightForWidth())
        self.Wing1_dock.setSizePolicy(sizePolicy)
        self.Wing1_dock.setMinimumSize(QSize(960, 840))
        self.Wing1_dock.setMaximumSize(QSize(960, 840))
        self.Wing1_dock.setFloating(False)
        self.Wing1_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea|Qt.DockWidgetArea.RightDockWidgetArea)
        self.Wing1_dock.setDockLocation(Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.gridLayout_2 = QGridLayout(self.dockWidgetContents_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button36 = QPushButton(self.dockWidgetContents_4)
        self.button36.setObjectName(u"button36")
        sizePolicy.setHeightForWidth(self.button36.sizePolicy().hasHeightForWidth())
        self.button36.setSizePolicy(sizePolicy)
        self.button36.setMinimumSize(QSize(88, 44))
        self.button36.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button36, 3, 5, 1, 1)

        self.button61 = QPushButton(self.dockWidgetContents_4)
        self.button61.setObjectName(u"button61")
        sizePolicy.setHeightForWidth(self.button61.sizePolicy().hasHeightForWidth())
        self.button61.setSizePolicy(sizePolicy)
        self.button61.setMinimumSize(QSize(88, 44))
        self.button61.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button61, 0, 6, 1, 1)

        self.button45 = QPushButton(self.dockWidgetContents_4)
        self.button45.setObjectName(u"button45")
        sizePolicy.setHeightForWidth(self.button45.sizePolicy().hasHeightForWidth())
        self.button45.setSizePolicy(sizePolicy)
        self.button45.setMinimumSize(QSize(88, 44))
        self.button45.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button45, 2, 6, 1, 1)

        self.button44 = QPushButton(self.dockWidgetContents_4)
        self.button44.setObjectName(u"button44")
        sizePolicy.setHeightForWidth(self.button44.sizePolicy().hasHeightForWidth())
        self.button44.setSizePolicy(sizePolicy)
        self.button44.setMinimumSize(QSize(88, 44))
        self.button44.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button44, 2, 5, 1, 1)

        self.button8 = QPushButton(self.dockWidgetContents_4)
        self.button8.setObjectName(u"button8")
        sizePolicy.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy)
        self.button8.setMinimumSize(QSize(88, 44))
        self.button8.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button8, 6, 1, 1, 1)

        self.button116_layout = QGridLayout()
        self.button116_layout.setObjectName(u"button116_layout")
        self.button116_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button116 = QPushButton(self.dockWidgetContents_4)
        self.button116.setObjectName(u"button116")
        self.button116.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button116.sizePolicy().hasHeightForWidth())
        self.button116.setSizePolicy(sizePolicy)
        self.button116.setMinimumSize(QSize(28, 28))
        self.button116.setMaximumSize(QSize(28, 28))
        font = QFont()
        font.setPointSize(6)
        self.button116.setFont(font)

        self.button116_layout.addWidget(self.button116, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button116_layout, 4, 10, 1, 1)

        self.button16 = QPushButton(self.dockWidgetContents_4)
        self.button16.setObjectName(u"button16")
        sizePolicy.setHeightForWidth(self.button16.sizePolicy().hasHeightForWidth())
        self.button16.setSizePolicy(sizePolicy)
        self.button16.setMinimumSize(QSize(88, 44))
        self.button16.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button16, 5, 1, 1, 1)

        self.button12 = QPushButton(self.dockWidgetContents_4)
        self.button12.setObjectName(u"button12")
        sizePolicy.setHeightForWidth(self.button12.sizePolicy().hasHeightForWidth())
        self.button12.setSizePolicy(sizePolicy)
        self.button12.setMinimumSize(QSize(88, 44))
        self.button12.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button12, 6, 5, 1, 1)

        self.button10 = QPushButton(self.dockWidgetContents_4)
        self.button10.setObjectName(u"button10")
        sizePolicy.setHeightForWidth(self.button10.sizePolicy().hasHeightForWidth())
        self.button10.setSizePolicy(sizePolicy)
        self.button10.setMinimumSize(QSize(88, 44))
        self.button10.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button10, 6, 3, 1, 1)

        self.button49 = QPushButton(self.dockWidgetContents_4)
        self.button49.setObjectName(u"button49")
        sizePolicy.setHeightForWidth(self.button49.sizePolicy().hasHeightForWidth())
        self.button49.setSizePolicy(sizePolicy)
        self.button49.setMinimumSize(QSize(88, 44))
        self.button49.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button49, 1, 2, 1, 1)

        self.button30 = QPushButton(self.dockWidgetContents_4)
        self.button30.setObjectName(u"button30")
        sizePolicy.setHeightForWidth(self.button30.sizePolicy().hasHeightForWidth())
        self.button30.setSizePolicy(sizePolicy)
        self.button30.setMinimumSize(QSize(88, 44))
        self.button30.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button30, 4, 7, 1, 1)

        self.button113_layout = QGridLayout()
        self.button113_layout.setObjectName(u"button113_layout")
        self.button113_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button113 = QPushButton(self.dockWidgetContents_4)
        self.button113.setObjectName(u"button113")
        self.button113.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button113.sizePolicy().hasHeightForWidth())
        self.button113.setSizePolicy(sizePolicy)
        self.button113.setMinimumSize(QSize(28, 28))
        self.button113.setMaximumSize(QSize(28, 28))
        self.button113.setFont(font)

        self.button113_layout.addWidget(self.button113, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button113_layout, 1, 10, 1, 1)

        self.button104_layout = QGridLayout()
        self.button104_layout.setObjectName(u"button104_layout")
        self.button104 = QPushButton(self.dockWidgetContents_4)
        self.button104.setObjectName(u"button104")
        self.button104.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button104.sizePolicy().hasHeightForWidth())
        self.button104.setSizePolicy(sizePolicy)
        self.button104.setMinimumSize(QSize(28, 28))
        self.button104.setMaximumSize(QSize(28, 28))
        self.button104.setFont(font)

        self.button104_layout.addWidget(self.button104, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button104_layout, 8, 5, 1, 1)

        self.button25 = QPushButton(self.dockWidgetContents_4)
        self.button25.setObjectName(u"button25")
        sizePolicy.setHeightForWidth(self.button25.sizePolicy().hasHeightForWidth())
        self.button25.setSizePolicy(sizePolicy)
        self.button25.setMinimumSize(QSize(88, 44))
        self.button25.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button25, 4, 2, 1, 1)

        self.button63 = QPushButton(self.dockWidgetContents_4)
        self.button63.setObjectName(u"button63")
        sizePolicy.setHeightForWidth(self.button63.sizePolicy().hasHeightForWidth())
        self.button63.setSizePolicy(sizePolicy)
        self.button63.setMinimumSize(QSize(88, 44))
        self.button63.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button63, 0, 8, 1, 1)

        self.button122_layout = QGridLayout()
        self.button122_layout.setObjectName(u"button122_layout")
        self.button122_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button122 = QPushButton(self.dockWidgetContents_4)
        self.button122.setObjectName(u"button122")
        self.button122.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button122.sizePolicy().hasHeightForWidth())
        self.button122.setSizePolicy(sizePolicy)
        self.button122.setMinimumSize(QSize(28, 28))
        self.button122.setMaximumSize(QSize(28, 28))
        self.button122.setFont(font)

        self.button122_layout.addWidget(self.button122, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button122_layout, 8, 10, 1, 1)

        self.button48 = QPushButton(self.dockWidgetContents_4)
        self.button48.setObjectName(u"button48")
        sizePolicy.setHeightForWidth(self.button48.sizePolicy().hasHeightForWidth())
        self.button48.setSizePolicy(sizePolicy)
        self.button48.setMinimumSize(QSize(88, 44))
        self.button48.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button48, 1, 1, 1, 1)

        self.button31 = QPushButton(self.dockWidgetContents_4)
        self.button31.setObjectName(u"button31")
        sizePolicy.setHeightForWidth(self.button31.sizePolicy().hasHeightForWidth())
        self.button31.setSizePolicy(sizePolicy)
        self.button31.setMinimumSize(QSize(88, 44))
        self.button31.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button31, 4, 8, 1, 1)

        self.button7 = QPushButton(self.dockWidgetContents_4)
        self.button7.setObjectName(u"button7")
        sizePolicy.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy)
        self.button7.setMinimumSize(QSize(88, 44))
        self.button7.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button7, 7, 8, 1, 1)

        self.button4 = QPushButton(self.dockWidgetContents_4)
        self.button4.setObjectName(u"button4")
        sizePolicy.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy)
        self.button4.setMinimumSize(QSize(88, 44))
        self.button4.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button4, 7, 5, 1, 1)

        self.button35 = QPushButton(self.dockWidgetContents_4)
        self.button35.setObjectName(u"button35")
        sizePolicy.setHeightForWidth(self.button35.sizePolicy().hasHeightForWidth())
        self.button35.setSizePolicy(sizePolicy)
        self.button35.setMinimumSize(QSize(88, 44))
        self.button35.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button35, 3, 4, 1, 1)

        self.button39 = QPushButton(self.dockWidgetContents_4)
        self.button39.setObjectName(u"button39")
        sizePolicy.setHeightForWidth(self.button39.sizePolicy().hasHeightForWidth())
        self.button39.setSizePolicy(sizePolicy)
        self.button39.setMinimumSize(QSize(88, 44))
        self.button39.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button39, 3, 8, 1, 1)

        self.button24 = QPushButton(self.dockWidgetContents_4)
        self.button24.setObjectName(u"button24")
        sizePolicy.setHeightForWidth(self.button24.sizePolicy().hasHeightForWidth())
        self.button24.setSizePolicy(sizePolicy)
        self.button24.setMinimumSize(QSize(88, 44))
        self.button24.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button24, 4, 1, 1, 1)

        self.button3 = QPushButton(self.dockWidgetContents_4)
        self.button3.setObjectName(u"button3")
        sizePolicy.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy)
        self.button3.setMinimumSize(QSize(88, 44))
        self.button3.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button3, 7, 4, 1, 1)

        self.button46 = QPushButton(self.dockWidgetContents_4)
        self.button46.setObjectName(u"button46")
        sizePolicy.setHeightForWidth(self.button46.sizePolicy().hasHeightForWidth())
        self.button46.setSizePolicy(sizePolicy)
        self.button46.setMinimumSize(QSize(88, 44))
        self.button46.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button46, 2, 7, 1, 1)

        self.button40 = QPushButton(self.dockWidgetContents_4)
        self.button40.setObjectName(u"button40")
        sizePolicy.setHeightForWidth(self.button40.sizePolicy().hasHeightForWidth())
        self.button40.setSizePolicy(sizePolicy)
        self.button40.setMinimumSize(QSize(88, 44))
        self.button40.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button40, 2, 1, 1, 1)

        self.button55 = QPushButton(self.dockWidgetContents_4)
        self.button55.setObjectName(u"button55")
        sizePolicy.setHeightForWidth(self.button55.sizePolicy().hasHeightForWidth())
        self.button55.setSizePolicy(sizePolicy)
        self.button55.setMinimumSize(QSize(88, 44))
        self.button55.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button55, 1, 8, 1, 1)

        self.button9 = QPushButton(self.dockWidgetContents_4)
        self.button9.setObjectName(u"button9")
        sizePolicy.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy)
        self.button9.setMinimumSize(QSize(88, 44))
        self.button9.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button9, 6, 2, 1, 1)

        self.button5 = QPushButton(self.dockWidgetContents_4)
        self.button5.setObjectName(u"button5")
        sizePolicy.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy)
        self.button5.setMinimumSize(QSize(88, 44))
        self.button5.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button5, 7, 6, 1, 1)

        self.button38 = QPushButton(self.dockWidgetContents_4)
        self.button38.setObjectName(u"button38")
        sizePolicy.setHeightForWidth(self.button38.sizePolicy().hasHeightForWidth())
        self.button38.setSizePolicy(sizePolicy)
        self.button38.setMinimumSize(QSize(88, 44))
        self.button38.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button38, 3, 7, 1, 1)

        self.button100_layout = QGridLayout()
        self.button100_layout.setObjectName(u"button100_layout")
        self.button100 = QPushButton(self.dockWidgetContents_4)
        self.button100.setObjectName(u"button100")
        self.button100.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button100.sizePolicy().hasHeightForWidth())
        self.button100.setSizePolicy(sizePolicy)
        self.button100.setMinimumSize(QSize(28, 28))
        self.button100.setMaximumSize(QSize(28, 28))
        self.button100.setFont(font)
        self.button100.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.button100.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.button100.setAutoDefault(False)

        self.button100_layout.addWidget(self.button100, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button100_layout, 8, 1, 1, 1)

        self.button119_layout = QGridLayout()
        self.button119_layout.setObjectName(u"button119_layout")
        self.button119_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button119 = QPushButton(self.dockWidgetContents_4)
        self.button119.setObjectName(u"button119")
        self.button119.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button119.sizePolicy().hasHeightForWidth())
        self.button119.setSizePolicy(sizePolicy)
        self.button119.setMinimumSize(QSize(28, 28))
        self.button119.setMaximumSize(QSize(28, 28))
        self.button119.setFont(font)

        self.button119_layout.addWidget(self.button119, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button119_layout, 7, 10, 1, 1)

        self.button52 = QPushButton(self.dockWidgetContents_4)
        self.button52.setObjectName(u"button52")
        sizePolicy.setHeightForWidth(self.button52.sizePolicy().hasHeightForWidth())
        self.button52.setSizePolicy(sizePolicy)
        self.button52.setMinimumSize(QSize(88, 44))
        self.button52.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button52, 1, 5, 1, 1)

        self.button51 = QPushButton(self.dockWidgetContents_4)
        self.button51.setObjectName(u"button51")
        sizePolicy.setHeightForWidth(self.button51.sizePolicy().hasHeightForWidth())
        self.button51.setSizePolicy(sizePolicy)
        self.button51.setMinimumSize(QSize(88, 44))
        self.button51.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button51, 1, 4, 1, 1)

        self.button60 = QPushButton(self.dockWidgetContents_4)
        self.button60.setObjectName(u"button60")
        sizePolicy.setHeightForWidth(self.button60.sizePolicy().hasHeightForWidth())
        self.button60.setSizePolicy(sizePolicy)
        self.button60.setMinimumSize(QSize(88, 44))
        self.button60.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button60, 0, 5, 1, 1)

        self.button13 = QPushButton(self.dockWidgetContents_4)
        self.button13.setObjectName(u"button13")
        sizePolicy.setHeightForWidth(self.button13.sizePolicy().hasHeightForWidth())
        self.button13.setSizePolicy(sizePolicy)
        self.button13.setMinimumSize(QSize(88, 44))
        self.button13.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button13, 6, 6, 1, 1)

        self.button14 = QPushButton(self.dockWidgetContents_4)
        self.button14.setObjectName(u"button14")
        sizePolicy.setHeightForWidth(self.button14.sizePolicy().hasHeightForWidth())
        self.button14.setSizePolicy(sizePolicy)
        self.button14.setMinimumSize(QSize(88, 44))
        self.button14.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button14, 6, 7, 1, 1)

        self.button6 = QPushButton(self.dockWidgetContents_4)
        self.button6.setObjectName(u"button6")
        sizePolicy.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy)
        self.button6.setMinimumSize(QSize(88, 44))
        self.button6.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button6, 7, 7, 1, 1)

        self.button26 = QPushButton(self.dockWidgetContents_4)
        self.button26.setObjectName(u"button26")
        sizePolicy.setHeightForWidth(self.button26.sizePolicy().hasHeightForWidth())
        self.button26.setSizePolicy(sizePolicy)
        self.button26.setMinimumSize(QSize(88, 44))
        self.button26.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button26, 4, 3, 1, 1)

        self.button1 = QPushButton(self.dockWidgetContents_4)
        self.button1.setObjectName(u"button1")
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setMinimumSize(QSize(88, 44))
        self.button1.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button1, 7, 2, 1, 1)

        self.button34 = QPushButton(self.dockWidgetContents_4)
        self.button34.setObjectName(u"button34")
        sizePolicy.setHeightForWidth(self.button34.sizePolicy().hasHeightForWidth())
        self.button34.setSizePolicy(sizePolicy)
        self.button34.setMinimumSize(QSize(88, 44))
        self.button34.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button34, 3, 3, 1, 1)

        self.button117_layout = QGridLayout()
        self.button117_layout.setObjectName(u"button117_layout")
        self.button117_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button117 = QPushButton(self.dockWidgetContents_4)
        self.button117.setObjectName(u"button117")
        self.button117.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button117.sizePolicy().hasHeightForWidth())
        self.button117.setSizePolicy(sizePolicy)
        self.button117.setMinimumSize(QSize(28, 28))
        self.button117.setMaximumSize(QSize(28, 28))
        self.button117.setFont(font)

        self.button117_layout.addWidget(self.button117, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button117_layout, 5, 10, 1, 1)

        self.button115_layout = QGridLayout()
        self.button115_layout.setObjectName(u"button115_layout")
        self.button115_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button115 = QPushButton(self.dockWidgetContents_4)
        self.button115.setObjectName(u"button115")
        self.button115.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button115.sizePolicy().hasHeightForWidth())
        self.button115.setSizePolicy(sizePolicy)
        self.button115.setMinimumSize(QSize(28, 28))
        self.button115.setMaximumSize(QSize(28, 28))
        self.button115.setFont(font)

        self.button115_layout.addWidget(self.button115, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button115_layout, 3, 10, 1, 1)

        self.button62 = QPushButton(self.dockWidgetContents_4)
        self.button62.setObjectName(u"button62")
        sizePolicy.setHeightForWidth(self.button62.sizePolicy().hasHeightForWidth())
        self.button62.setSizePolicy(sizePolicy)
        self.button62.setMinimumSize(QSize(88, 44))
        self.button62.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button62, 0, 7, 1, 1)

        self.button58 = QPushButton(self.dockWidgetContents_4)
        self.button58.setObjectName(u"button58")
        sizePolicy.setHeightForWidth(self.button58.sizePolicy().hasHeightForWidth())
        self.button58.setSizePolicy(sizePolicy)
        self.button58.setMinimumSize(QSize(88, 44))
        self.button58.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button58, 0, 3, 1, 1)

        self.button29 = QPushButton(self.dockWidgetContents_4)
        self.button29.setObjectName(u"button29")
        sizePolicy.setHeightForWidth(self.button29.sizePolicy().hasHeightForWidth())
        self.button29.setSizePolicy(sizePolicy)
        self.button29.setMinimumSize(QSize(88, 44))
        self.button29.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button29, 4, 6, 1, 1)

        self.button21 = QPushButton(self.dockWidgetContents_4)
        self.button21.setObjectName(u"button21")
        sizePolicy.setHeightForWidth(self.button21.sizePolicy().hasHeightForWidth())
        self.button21.setSizePolicy(sizePolicy)
        self.button21.setMinimumSize(QSize(88, 44))
        self.button21.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button21, 5, 6, 1, 1)

        self.button43 = QPushButton(self.dockWidgetContents_4)
        self.button43.setObjectName(u"button43")
        sizePolicy.setHeightForWidth(self.button43.sizePolicy().hasHeightForWidth())
        self.button43.setSizePolicy(sizePolicy)
        self.button43.setMinimumSize(QSize(88, 44))
        self.button43.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button43, 2, 4, 1, 1)

        self.button15 = QPushButton(self.dockWidgetContents_4)
        self.button15.setObjectName(u"button15")
        sizePolicy.setHeightForWidth(self.button15.sizePolicy().hasHeightForWidth())
        self.button15.setSizePolicy(sizePolicy)
        self.button15.setMinimumSize(QSize(88, 44))
        self.button15.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button15, 6, 8, 1, 1)

        self.right_padding2 = QSpacerItem(0, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.right_padding2, 7, 11, 1, 1)

        self.button32 = QPushButton(self.dockWidgetContents_4)
        self.button32.setObjectName(u"button32")
        sizePolicy.setHeightForWidth(self.button32.sizePolicy().hasHeightForWidth())
        self.button32.setSizePolicy(sizePolicy)
        self.button32.setMinimumSize(QSize(88, 44))
        self.button32.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button32, 3, 1, 1, 1)

        self.button59 = QPushButton(self.dockWidgetContents_4)
        self.button59.setObjectName(u"button59")
        sizePolicy.setHeightForWidth(self.button59.sizePolicy().hasHeightForWidth())
        self.button59.setSizePolicy(sizePolicy)
        self.button59.setMinimumSize(QSize(88, 44))
        self.button59.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button59, 0, 4, 1, 1)

        self.button118_layout = QGridLayout()
        self.button118_layout.setObjectName(u"button118_layout")
        self.button118_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button118 = QPushButton(self.dockWidgetContents_4)
        self.button118.setObjectName(u"button118")
        self.button118.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button118.sizePolicy().hasHeightForWidth())
        self.button118.setSizePolicy(sizePolicy)
        self.button118.setMinimumSize(QSize(28, 28))
        self.button118.setMaximumSize(QSize(28, 28))
        self.button118.setFont(font)

        self.button118_layout.addWidget(self.button118, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button118_layout, 6, 10, 1, 1)

        self.button22 = QPushButton(self.dockWidgetContents_4)
        self.button22.setObjectName(u"button22")
        sizePolicy.setHeightForWidth(self.button22.sizePolicy().hasHeightForWidth())
        self.button22.setSizePolicy(sizePolicy)
        self.button22.setMinimumSize(QSize(88, 44))
        self.button22.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button22, 5, 7, 1, 1)

        self.button42 = QPushButton(self.dockWidgetContents_4)
        self.button42.setObjectName(u"button42")
        sizePolicy.setHeightForWidth(self.button42.sizePolicy().hasHeightForWidth())
        self.button42.setSizePolicy(sizePolicy)
        self.button42.setMinimumSize(QSize(88, 44))
        self.button42.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button42, 2, 3, 1, 1)

        self.button107_layout = QGridLayout()
        self.button107_layout.setObjectName(u"button107_layout")
        self.button107 = QPushButton(self.dockWidgetContents_4)
        self.button107.setObjectName(u"button107")
        self.button107.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button107.sizePolicy().hasHeightForWidth())
        self.button107.setSizePolicy(sizePolicy)
        self.button107.setMinimumSize(QSize(28, 28))
        self.button107.setMaximumSize(QSize(28, 28))
        self.button107.setFont(font)

        self.button107_layout.addWidget(self.button107, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button107_layout, 8, 8, 1, 1)

        self.right_padding = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.right_padding, 8, 11, 1, 1)

        self.button27 = QPushButton(self.dockWidgetContents_4)
        self.button27.setObjectName(u"button27")
        sizePolicy.setHeightForWidth(self.button27.sizePolicy().hasHeightForWidth())
        self.button27.setSizePolicy(sizePolicy)
        self.button27.setMinimumSize(QSize(88, 44))
        self.button27.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button27, 4, 4, 1, 1)

        self.frame_fader52 = QFrame(self.dockWidgetContents_4)
        self.frame_fader52.setObjectName(u"frame_fader52")
        self.frame_fader52.setMinimumSize(QSize(88, 250))
        self.frame_fader52.setMaximumSize(QSize(88, 250))
        self.frame_fader52.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader52.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_fader52)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader52 = QGridLayout()
        self.below_button_layout_fader52.setSpacing(0)
        self.below_button_layout_fader52.setObjectName(u"below_button_layout_fader52")
        self.fader52_layout = QGridLayout()
        self.fader52_layout.setObjectName(u"fader52_layout")
        self.fader52 = QSlider(self.frame_fader52)
        self.fader52.setObjectName(u"fader52")
        sizePolicy.setHeightForWidth(self.fader52.sizePolicy().hasHeightForWidth())
        self.fader52.setSizePolicy(sizePolicy)
        self.fader52.setMinimumSize(QSize(0, 190))
        self.fader52.setMaximumSize(QSize(15, 190))
        self.fader52.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader52.setAutoFillBackground(False)
        self.fader52.setMaximum(127)
        self.fader52.setSliderPosition(0)
        self.fader52.setOrientation(Qt.Orientation.Vertical)
        self.fader52.setInvertedAppearance(False)
        self.fader52.setInvertedControls(False)

        self.fader52_layout.addWidget(self.fader52, 0, 0, 1, 1)


        self.below_button_layout_fader52.addLayout(self.fader52_layout, 0, 0, 1, 1)

        self.pushButton_fader52 = QPushButton(self.frame_fader52)
        self.pushButton_fader52.setObjectName(u"pushButton_fader52")

        self.below_button_layout_fader52.addWidget(self.pushButton_fader52, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader52.addItem(self.verticalSpacer_5, 1, 0, 1, 1)


        self.gridLayout_17.addLayout(self.below_button_layout_fader52, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fader52, 10, 5, 1, 1)

        self.button17 = QPushButton(self.dockWidgetContents_4)
        self.button17.setObjectName(u"button17")
        sizePolicy.setHeightForWidth(self.button17.sizePolicy().hasHeightForWidth())
        self.button17.setSizePolicy(sizePolicy)
        self.button17.setMinimumSize(QSize(88, 44))
        self.button17.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button17, 5, 2, 1, 1)

        self.frame_fader53 = QFrame(self.dockWidgetContents_4)
        self.frame_fader53.setObjectName(u"frame_fader53")
        self.frame_fader53.setMinimumSize(QSize(88, 250))
        self.frame_fader53.setMaximumSize(QSize(88, 250))
        self.frame_fader53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader53.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_fader53)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader53 = QGridLayout()
        self.below_button_layout_fader53.setSpacing(0)
        self.below_button_layout_fader53.setObjectName(u"below_button_layout_fader53")
        self.fader53_layout = QGridLayout()
        self.fader53_layout.setObjectName(u"fader53_layout")
        self.fader53 = QSlider(self.frame_fader53)
        self.fader53.setObjectName(u"fader53")
        sizePolicy.setHeightForWidth(self.fader53.sizePolicy().hasHeightForWidth())
        self.fader53.setSizePolicy(sizePolicy)
        self.fader53.setMinimumSize(QSize(0, 190))
        self.fader53.setMaximumSize(QSize(15, 190))
        self.fader53.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader53.setAutoFillBackground(False)
        self.fader53.setMaximum(127)
        self.fader53.setSliderPosition(0)
        self.fader53.setOrientation(Qt.Orientation.Vertical)
        self.fader53.setInvertedAppearance(False)
        self.fader53.setInvertedControls(False)

        self.fader53_layout.addWidget(self.fader53, 0, 0, 1, 1)


        self.below_button_layout_fader53.addLayout(self.fader53_layout, 0, 0, 1, 1)

        self.pushButton_fader53 = QPushButton(self.frame_fader53)
        self.pushButton_fader53.setObjectName(u"pushButton_fader53")

        self.below_button_layout_fader53.addWidget(self.pushButton_fader53, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader53.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.gridLayout_18.addLayout(self.below_button_layout_fader53, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fader53, 10, 6, 1, 1)

        self.frame_fader49 = QFrame(self.dockWidgetContents_4)
        self.frame_fader49.setObjectName(u"frame_fader49")
        self.frame_fader49.setMinimumSize(QSize(88, 250))
        self.frame_fader49.setMaximumSize(QSize(88, 250))
        self.frame_fader49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader49.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_fader49)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader49 = QGridLayout()
        self.below_button_layout_fader49.setSpacing(0)
        self.below_button_layout_fader49.setObjectName(u"below_button_layout_fader49")
        self.pushButton_fader49 = QPushButton(self.frame_fader49)
        self.pushButton_fader49.setObjectName(u"pushButton_fader49")

        self.below_button_layout_fader49.addWidget(self.pushButton_fader49, 2, 0, 1, 1)

        self.fader49_layout = QGridLayout()
        self.fader49_layout.setObjectName(u"fader49_layout")
        self.fader49 = QSlider(self.frame_fader49)
        self.fader49.setObjectName(u"fader49")
        sizePolicy.setHeightForWidth(self.fader49.sizePolicy().hasHeightForWidth())
        self.fader49.setSizePolicy(sizePolicy)
        self.fader49.setMinimumSize(QSize(0, 190))
        self.fader49.setMaximumSize(QSize(15, 190))
        self.fader49.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader49.setAutoFillBackground(False)
        self.fader49.setMaximum(127)
        self.fader49.setSliderPosition(0)
        self.fader49.setOrientation(Qt.Orientation.Vertical)
        self.fader49.setInvertedAppearance(False)
        self.fader49.setInvertedControls(False)

        self.fader49_layout.addWidget(self.fader49, 0, 0, 1, 1)


        self.below_button_layout_fader49.addLayout(self.fader49_layout, 0, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader49.addItem(self.verticalSpacer_8, 1, 0, 1, 1)


        self.gridLayout_14.addLayout(self.below_button_layout_fader49, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fader49, 10, 2, 1, 1)

        self.button37 = QPushButton(self.dockWidgetContents_4)
        self.button37.setObjectName(u"button37")
        sizePolicy.setHeightForWidth(self.button37.sizePolicy().hasHeightForWidth())
        self.button37.setSizePolicy(sizePolicy)
        self.button37.setMinimumSize(QSize(88, 44))
        self.button37.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button37, 3, 6, 1, 1)

        self.button41 = QPushButton(self.dockWidgetContents_4)
        self.button41.setObjectName(u"button41")
        sizePolicy.setHeightForWidth(self.button41.sizePolicy().hasHeightForWidth())
        self.button41.setSizePolicy(sizePolicy)
        self.button41.setMinimumSize(QSize(88, 44))
        self.button41.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button41, 2, 2, 1, 1)

        self.button0 = QPushButton(self.dockWidgetContents_4)
        self.button0.setObjectName(u"button0")
        sizePolicy.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy)
        self.button0.setMinimumSize(QSize(88, 44))
        self.button0.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button0, 7, 1, 1, 1)

        self.left_padding_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.left_padding_2, 7, 0, 1, 1)

        self.button56 = QPushButton(self.dockWidgetContents_4)
        self.button56.setObjectName(u"button56")
        sizePolicy.setHeightForWidth(self.button56.sizePolicy().hasHeightForWidth())
        self.button56.setSizePolicy(sizePolicy)
        self.button56.setMinimumSize(QSize(88, 44))
        self.button56.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button56, 0, 1, 1, 1)

        self.button23 = QPushButton(self.dockWidgetContents_4)
        self.button23.setObjectName(u"button23")
        sizePolicy.setHeightForWidth(self.button23.sizePolicy().hasHeightForWidth())
        self.button23.setSizePolicy(sizePolicy)
        self.button23.setMinimumSize(QSize(88, 44))
        self.button23.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button23, 5, 8, 1, 1)

        self.button54 = QPushButton(self.dockWidgetContents_4)
        self.button54.setObjectName(u"button54")
        sizePolicy.setHeightForWidth(self.button54.sizePolicy().hasHeightForWidth())
        self.button54.setSizePolicy(sizePolicy)
        self.button54.setMinimumSize(QSize(88, 44))
        self.button54.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button54, 1, 7, 1, 1)

        self.frame_fader48 = QFrame(self.dockWidgetContents_4)
        self.frame_fader48.setObjectName(u"frame_fader48")
        self.frame_fader48.setMinimumSize(QSize(88, 250))
        self.frame_fader48.setMaximumSize(QSize(88, 250))
        self.frame_fader48.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader48.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_fader48)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader48 = QGridLayout()
        self.below_button_layout_fader48.setSpacing(0)
        self.below_button_layout_fader48.setObjectName(u"below_button_layout_fader48")
        self.fader48_layout = QGridLayout()
        self.fader48_layout.setObjectName(u"fader48_layout")
        self.fader48 = QSlider(self.frame_fader48)
        self.fader48.setObjectName(u"fader48")
        sizePolicy.setHeightForWidth(self.fader48.sizePolicy().hasHeightForWidth())
        self.fader48.setSizePolicy(sizePolicy)
        self.fader48.setMinimumSize(QSize(0, 190))
        self.fader48.setMaximumSize(QSize(15, 190))
        self.fader48.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader48.setAutoFillBackground(False)
        self.fader48.setMaximum(127)
        self.fader48.setSliderPosition(0)
        self.fader48.setOrientation(Qt.Orientation.Vertical)
        self.fader48.setInvertedAppearance(False)
        self.fader48.setInvertedControls(False)

        self.fader48_layout.addWidget(self.fader48, 0, 0, 1, 1)


        self.below_button_layout_fader48.addLayout(self.fader48_layout, 0, 0, 1, 1)

        self.pushButton_fader48 = QPushButton(self.frame_fader48)
        self.pushButton_fader48.setObjectName(u"pushButton_fader48")

        self.below_button_layout_fader48.addWidget(self.pushButton_fader48, 2, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader48.addItem(self.verticalSpacer_9, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.below_button_layout_fader48, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fader48, 10, 1, 1, 1)

        self.button106_layout = QGridLayout()
        self.button106_layout.setObjectName(u"button106_layout")
        self.button106 = QPushButton(self.dockWidgetContents_4)
        self.button106.setObjectName(u"button106")
        self.button106.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button106.sizePolicy().hasHeightForWidth())
        self.button106.setSizePolicy(sizePolicy)
        self.button106.setMinimumSize(QSize(28, 28))
        self.button106.setMaximumSize(QSize(28, 28))
        self.button106.setFont(font)

        self.button106_layout.addWidget(self.button106, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button106_layout, 8, 7, 1, 1)

        self.button33 = QPushButton(self.dockWidgetContents_4)
        self.button33.setObjectName(u"button33")
        sizePolicy.setHeightForWidth(self.button33.sizePolicy().hasHeightForWidth())
        self.button33.setSizePolicy(sizePolicy)
        self.button33.setMinimumSize(QSize(88, 44))
        self.button33.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button33, 3, 2, 1, 1)

        self.button28 = QPushButton(self.dockWidgetContents_4)
        self.button28.setObjectName(u"button28")
        sizePolicy.setHeightForWidth(self.button28.sizePolicy().hasHeightForWidth())
        self.button28.setSizePolicy(sizePolicy)
        self.button28.setMinimumSize(QSize(88, 44))
        self.button28.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button28, 4, 5, 1, 1)

        self.button2 = QPushButton(self.dockWidgetContents_4)
        self.button2.setObjectName(u"button2")
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        self.button2.setMinimumSize(QSize(88, 44))
        self.button2.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button2, 7, 3, 1, 1)

        self.button11 = QPushButton(self.dockWidgetContents_4)
        self.button11.setObjectName(u"button11")
        sizePolicy.setHeightForWidth(self.button11.sizePolicy().hasHeightForWidth())
        self.button11.setSizePolicy(sizePolicy)
        self.button11.setMinimumSize(QSize(88, 44))
        self.button11.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button11, 6, 4, 1, 1)

        self.button102_layout = QGridLayout()
        self.button102_layout.setObjectName(u"button102_layout")
        self.button102 = QPushButton(self.dockWidgetContents_4)
        self.button102.setObjectName(u"button102")
        self.button102.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button102.sizePolicy().hasHeightForWidth())
        self.button102.setSizePolicy(sizePolicy)
        self.button102.setMinimumSize(QSize(28, 28))
        self.button102.setMaximumSize(QSize(28, 28))
        self.button102.setFont(font)

        self.button102_layout.addWidget(self.button102, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button102_layout, 8, 3, 1, 1)

        self.button18 = QPushButton(self.dockWidgetContents_4)
        self.button18.setObjectName(u"button18")
        sizePolicy.setHeightForWidth(self.button18.sizePolicy().hasHeightForWidth())
        self.button18.setSizePolicy(sizePolicy)
        self.button18.setMinimumSize(QSize(88, 44))
        self.button18.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button18, 5, 3, 1, 1)

        self.button19 = QPushButton(self.dockWidgetContents_4)
        self.button19.setObjectName(u"button19")
        sizePolicy.setHeightForWidth(self.button19.sizePolicy().hasHeightForWidth())
        self.button19.setSizePolicy(sizePolicy)
        self.button19.setMinimumSize(QSize(88, 44))
        self.button19.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button19, 5, 4, 1, 1)

        self.button47 = QPushButton(self.dockWidgetContents_4)
        self.button47.setObjectName(u"button47")
        sizePolicy.setHeightForWidth(self.button47.sizePolicy().hasHeightForWidth())
        self.button47.setSizePolicy(sizePolicy)
        self.button47.setMinimumSize(QSize(88, 44))
        self.button47.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button47, 2, 8, 1, 1)

        self.button53 = QPushButton(self.dockWidgetContents_4)
        self.button53.setObjectName(u"button53")
        sizePolicy.setHeightForWidth(self.button53.sizePolicy().hasHeightForWidth())
        self.button53.setSizePolicy(sizePolicy)
        self.button53.setMinimumSize(QSize(88, 44))
        self.button53.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button53, 1, 6, 1, 1)

        self.button112_layout = QGridLayout()
        self.button112_layout.setObjectName(u"button112_layout")
        self.button112_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button112 = QPushButton(self.dockWidgetContents_4)
        self.button112.setObjectName(u"button112")
        self.button112.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button112.sizePolicy().hasHeightForWidth())
        self.button112.setSizePolicy(sizePolicy)
        self.button112.setMinimumSize(QSize(28, 28))
        self.button112.setMaximumSize(QSize(28, 28))
        self.button112.setFont(font)

        self.button112_layout.addWidget(self.button112, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button112_layout, 0, 10, 1, 1)

        self.button114_layout = QGridLayout()
        self.button114_layout.setObjectName(u"button114_layout")
        self.button114_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button114 = QPushButton(self.dockWidgetContents_4)
        self.button114.setObjectName(u"button114")
        self.button114.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button114.sizePolicy().hasHeightForWidth())
        self.button114.setSizePolicy(sizePolicy)
        self.button114.setMinimumSize(QSize(28, 28))
        self.button114.setMaximumSize(QSize(28, 28))
        self.button114.setFont(font)

        self.button114_layout.addWidget(self.button114, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button114_layout, 2, 10, 1, 1)

        self.button50 = QPushButton(self.dockWidgetContents_4)
        self.button50.setObjectName(u"button50")
        sizePolicy.setHeightForWidth(self.button50.sizePolicy().hasHeightForWidth())
        self.button50.setSizePolicy(sizePolicy)
        self.button50.setMinimumSize(QSize(88, 44))
        self.button50.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button50, 1, 3, 1, 1)

        self.left_padding = QSpacerItem(0, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.left_padding, 8, 0, 1, 1)

        self.frame_fader51 = QFrame(self.dockWidgetContents_4)
        self.frame_fader51.setObjectName(u"frame_fader51")
        self.frame_fader51.setMinimumSize(QSize(88, 250))
        self.frame_fader51.setMaximumSize(QSize(88, 250))
        self.frame_fader51.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader51.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_fader51)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader51 = QGridLayout()
        self.below_button_layout_fader51.setSpacing(0)
        self.below_button_layout_fader51.setObjectName(u"below_button_layout_fader51")
        self.fader51_layout = QGridLayout()
        self.fader51_layout.setObjectName(u"fader51_layout")
        self.fader51 = QSlider(self.frame_fader51)
        self.fader51.setObjectName(u"fader51")
        sizePolicy.setHeightForWidth(self.fader51.sizePolicy().hasHeightForWidth())
        self.fader51.setSizePolicy(sizePolicy)
        self.fader51.setMinimumSize(QSize(0, 190))
        self.fader51.setMaximumSize(QSize(15, 190))
        self.fader51.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader51.setAutoFillBackground(False)
        self.fader51.setMaximum(127)
        self.fader51.setSliderPosition(0)
        self.fader51.setOrientation(Qt.Orientation.Vertical)
        self.fader51.setInvertedAppearance(False)
        self.fader51.setInvertedControls(False)

        self.fader51_layout.addWidget(self.fader51, 0, 0, 1, 1)


        self.below_button_layout_fader51.addLayout(self.fader51_layout, 0, 0, 1, 1)

        self.pushButton_fader51 = QPushButton(self.frame_fader51)
        self.pushButton_fader51.setObjectName(u"pushButton_fader51")

        self.below_button_layout_fader51.addWidget(self.pushButton_fader51, 2, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader51.addItem(self.verticalSpacer_6, 1, 0, 1, 1)


        self.gridLayout_16.addLayout(self.below_button_layout_fader51, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fader51, 10, 4, 1, 1)

        self.frame_fader50 = QFrame(self.dockWidgetContents_4)
        self.frame_fader50.setObjectName(u"frame_fader50")
        self.frame_fader50.setMinimumSize(QSize(88, 250))
        self.frame_fader50.setMaximumSize(QSize(88, 250))
        self.frame_fader50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader50.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_fader50)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader50 = QGridLayout()
        self.below_button_layout_fader50.setSpacing(0)
        self.below_button_layout_fader50.setObjectName(u"below_button_layout_fader50")
        self.pushButton_fader50 = QPushButton(self.frame_fader50)
        self.pushButton_fader50.setObjectName(u"pushButton_fader50")

        self.below_button_layout_fader50.addWidget(self.pushButton_fader50, 2, 0, 1, 1)

        self.fader50_layout = QGridLayout()
        self.fader50_layout.setObjectName(u"fader50_layout")
        self.fader50 = QSlider(self.frame_fader50)
        self.fader50.setObjectName(u"fader50")
        sizePolicy.setHeightForWidth(self.fader50.sizePolicy().hasHeightForWidth())
        self.fader50.setSizePolicy(sizePolicy)
        self.fader50.setMinimumSize(QSize(0, 190))
        self.fader50.setMaximumSize(QSize(15, 190))
        self.fader50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader50.setAutoFillBackground(False)
        self.fader50.setMaximum(127)
        self.fader50.setSliderPosition(0)
        self.fader50.setOrientation(Qt.Orientation.Vertical)
        self.fader50.setInvertedAppearance(False)
        self.fader50.setInvertedControls(False)

        self.fader50_layout.addWidget(self.fader50, 0, 0, 1, 1)


        self.below_button_layout_fader50.addLayout(self.fader50_layout, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader50.addItem(self.verticalSpacer_7, 1, 0, 1, 1)


        self.gridLayout_15.addLayout(self.below_button_layout_fader50, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fader50, 10, 3, 1, 1)

        self.button105_layout = QGridLayout()
        self.button105_layout.setObjectName(u"button105_layout")
        self.button105 = QPushButton(self.dockWidgetContents_4)
        self.button105.setObjectName(u"button105")
        self.button105.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button105.sizePolicy().hasHeightForWidth())
        self.button105.setSizePolicy(sizePolicy)
        self.button105.setMinimumSize(QSize(28, 28))
        self.button105.setMaximumSize(QSize(28, 28))
        self.button105.setFont(font)

        self.button105_layout.addWidget(self.button105, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button105_layout, 8, 6, 1, 1)

        self.button20 = QPushButton(self.dockWidgetContents_4)
        self.button20.setObjectName(u"button20")
        sizePolicy.setHeightForWidth(self.button20.sizePolicy().hasHeightForWidth())
        self.button20.setSizePolicy(sizePolicy)
        self.button20.setMinimumSize(QSize(88, 44))
        self.button20.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button20, 5, 5, 1, 1)

        self.button101_layout = QGridLayout()
        self.button101_layout.setObjectName(u"button101_layout")
        self.button101 = QPushButton(self.dockWidgetContents_4)
        self.button101.setObjectName(u"button101")
        self.button101.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button101.sizePolicy().hasHeightForWidth())
        self.button101.setSizePolicy(sizePolicy)
        self.button101.setMinimumSize(QSize(28, 28))
        self.button101.setMaximumSize(QSize(28, 28))
        self.button101.setFont(font)

        self.button101_layout.addWidget(self.button101, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button101_layout, 8, 2, 1, 1)

        self.button103_layout = QGridLayout()
        self.button103_layout.setObjectName(u"button103_layout")
        self.button103 = QPushButton(self.dockWidgetContents_4)
        self.button103.setObjectName(u"button103")
        self.button103.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button103.sizePolicy().hasHeightForWidth())
        self.button103.setSizePolicy(sizePolicy)
        self.button103.setMinimumSize(QSize(28, 28))
        self.button103.setMaximumSize(QSize(28, 28))
        self.button103.setFont(font)

        self.button103_layout.addWidget(self.button103, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.button103_layout, 8, 4, 1, 1)

        self.button57 = QPushButton(self.dockWidgetContents_4)
        self.button57.setObjectName(u"button57")
        sizePolicy.setHeightForWidth(self.button57.sizePolicy().hasHeightForWidth())
        self.button57.setSizePolicy(sizePolicy)
        self.button57.setMinimumSize(QSize(88, 44))
        self.button57.setMaximumSize(QSize(88, 44))

        self.gridLayout_2.addWidget(self.button57, 0, 2, 1, 1)

        self.frame_fader54 = QFrame(self.dockWidgetContents_4)
        self.frame_fader54.setObjectName(u"frame_fader54")
        self.frame_fader54.setMinimumSize(QSize(88, 250))
        self.frame_fader54.setMaximumSize(QSize(88, 250))
        self.frame_fader54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader54.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_fader54)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader54 = QGridLayout()
        self.below_button_layout_fader54.setSpacing(0)
        self.below_button_layout_fader54.setObjectName(u"below_button_layout_fader54")
        self.pushButton_fader54 = QPushButton(self.frame_fader54)
        self.pushButton_fader54.setObjectName(u"pushButton_fader54")

        self.below_button_layout_fader54.addWidget(self.pushButton_fader54, 2, 0, 1, 1)

        self.fader54_layout = QGridLayout()
        self.fader54_layout.setObjectName(u"fader54_layout")
        self.fader54 = QSlider(self.frame_fader54)
        self.fader54.setObjectName(u"fader54")
        sizePolicy.setHeightForWidth(self.fader54.sizePolicy().hasHeightForWidth())
        self.fader54.setSizePolicy(sizePolicy)
        self.fader54.setMinimumSize(QSize(0, 190))
        self.fader54.setMaximumSize(QSize(15, 190))
        self.fader54.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader54.setAutoFillBackground(False)
        self.fader54.setMaximum(127)
        self.fader54.setSliderPosition(0)
        self.fader54.setOrientation(Qt.Orientation.Vertical)
        self.fader54.setInvertedAppearance(False)
        self.fader54.setInvertedControls(False)

        self.fader54_layout.addWidget(self.fader54, 0, 0, 1, 1)


        self.below_button_layout_fader54.addLayout(self.fader54_layout, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader54.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.gridLayout_20.addLayout(self.below_button_layout_fader54, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fader54, 10, 7, 1, 1)

        self.frame_fader55 = QFrame(self.dockWidgetContents_4)
        self.frame_fader55.setObjectName(u"frame_fader55")
        self.frame_fader55.setMinimumSize(QSize(88, 250))
        self.frame_fader55.setMaximumSize(QSize(88, 250))
        self.frame_fader55.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader55.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_fader55)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader55 = QGridLayout()
        self.below_button_layout_fader55.setSpacing(0)
        self.below_button_layout_fader55.setObjectName(u"below_button_layout_fader55")
        self.fader55_layout = QGridLayout()
        self.fader55_layout.setObjectName(u"fader55_layout")
        self.fader55 = QSlider(self.frame_fader55)
        self.fader55.setObjectName(u"fader55")
        sizePolicy.setHeightForWidth(self.fader55.sizePolicy().hasHeightForWidth())
        self.fader55.setSizePolicy(sizePolicy)
        self.fader55.setMinimumSize(QSize(0, 190))
        self.fader55.setMaximumSize(QSize(15, 190))
        self.fader55.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader55.setAutoFillBackground(False)
        self.fader55.setMaximum(127)
        self.fader55.setSliderPosition(0)
        self.fader55.setOrientation(Qt.Orientation.Vertical)
        self.fader55.setInvertedAppearance(False)
        self.fader55.setInvertedControls(False)

        self.fader55_layout.addWidget(self.fader55, 0, 0, 1, 1)


        self.below_button_layout_fader55.addLayout(self.fader55_layout, 0, 0, 1, 1)

        self.pushButton_fader55 = QPushButton(self.frame_fader55)
        self.pushButton_fader55.setObjectName(u"pushButton_fader55")

        self.below_button_layout_fader55.addWidget(self.pushButton_fader55, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader55.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout_21.addLayout(self.below_button_layout_fader55, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fader55, 10, 8, 1, 1)

        self.frame_fader56 = QFrame(self.dockWidgetContents_4)
        self.frame_fader56.setObjectName(u"frame_fader56")
        self.frame_fader56.setMinimumSize(QSize(88, 250))
        self.frame_fader56.setMaximumSize(QSize(88, 250))
        self.frame_fader56.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader56.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_fader56)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader56 = QGridLayout()
        self.below_button_layout_fader56.setSpacing(0)
        self.below_button_layout_fader56.setObjectName(u"below_button_layout_fader56")
        self.fader56_layout = QGridLayout()
        self.fader56_layout.setObjectName(u"fader56_layout")
        self.fader56 = QSlider(self.frame_fader56)
        self.fader56.setObjectName(u"fader56")
        sizePolicy.setHeightForWidth(self.fader56.sizePolicy().hasHeightForWidth())
        self.fader56.setSizePolicy(sizePolicy)
        self.fader56.setMinimumSize(QSize(0, 190))
        self.fader56.setMaximumSize(QSize(15, 190))
        self.fader56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader56.setAutoFillBackground(False)
        self.fader56.setMaximum(127)
        self.fader56.setSliderPosition(0)
        self.fader56.setOrientation(Qt.Orientation.Vertical)
        self.fader56.setInvertedAppearance(False)
        self.fader56.setInvertedControls(False)

        self.fader56_layout.addWidget(self.fader56, 0, 0, 1, 1)


        self.below_button_layout_fader56.addLayout(self.fader56_layout, 0, 0, 1, 1)

        self.pushButton_fader56 = QPushButton(self.frame_fader56)
        self.pushButton_fader56.setObjectName(u"pushButton_fader56")

        self.below_button_layout_fader56.addWidget(self.pushButton_fader56, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader56.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_22.addLayout(self.below_button_layout_fader56, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fader56, 10, 10, 1, 1)

        self.Wing1_dock.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.Wing1_dock)
        self.Wing2_dock = QDockWidget(MainWindow)
        self.Wing2_dock.setObjectName(u"Wing2_dock")
        sizePolicy.setHeightForWidth(self.Wing2_dock.sizePolicy().hasHeightForWidth())
        self.Wing2_dock.setSizePolicy(sizePolicy)
        self.Wing2_dock.setMinimumSize(QSize(960, 840))
        self.Wing2_dock.setMaximumSize(QSize(960, 840))
        self.Wing2_dock.setFloating(False)
        self.Wing2_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea|Qt.DockWidgetArea.RightDockWidgetArea)
        self.Wing2_dock.setDockLocation(Qt.DockWidgetArea.LeftDockWidgetArea)
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.gridLayout_3 = QGridLayout(self.dockWidgetContents_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.button36_2 = QPushButton(self.dockWidgetContents_5)
        self.button36_2.setObjectName(u"button36_2")
        sizePolicy.setHeightForWidth(self.button36_2.sizePolicy().hasHeightForWidth())
        self.button36_2.setSizePolicy(sizePolicy)
        self.button36_2.setMinimumSize(QSize(88, 44))
        self.button36_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button36_2, 3, 5, 1, 1)

        self.button61_2 = QPushButton(self.dockWidgetContents_5)
        self.button61_2.setObjectName(u"button61_2")
        sizePolicy.setHeightForWidth(self.button61_2.sizePolicy().hasHeightForWidth())
        self.button61_2.setSizePolicy(sizePolicy)
        self.button61_2.setMinimumSize(QSize(88, 44))
        self.button61_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button61_2, 0, 6, 1, 1)

        self.button45_2 = QPushButton(self.dockWidgetContents_5)
        self.button45_2.setObjectName(u"button45_2")
        sizePolicy.setHeightForWidth(self.button45_2.sizePolicy().hasHeightForWidth())
        self.button45_2.setSizePolicy(sizePolicy)
        self.button45_2.setMinimumSize(QSize(88, 44))
        self.button45_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button45_2, 2, 6, 1, 1)

        self.button44_2 = QPushButton(self.dockWidgetContents_5)
        self.button44_2.setObjectName(u"button44_2")
        sizePolicy.setHeightForWidth(self.button44_2.sizePolicy().hasHeightForWidth())
        self.button44_2.setSizePolicy(sizePolicy)
        self.button44_2.setMinimumSize(QSize(88, 44))
        self.button44_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button44_2, 2, 5, 1, 1)

        self.button8_2 = QPushButton(self.dockWidgetContents_5)
        self.button8_2.setObjectName(u"button8_2")
        sizePolicy.setHeightForWidth(self.button8_2.sizePolicy().hasHeightForWidth())
        self.button8_2.setSizePolicy(sizePolicy)
        self.button8_2.setMinimumSize(QSize(88, 44))
        self.button8_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button8_2, 6, 1, 1, 1)

        self.button116_layout_2 = QGridLayout()
        self.button116_layout_2.setObjectName(u"button116_layout_2")
        self.button116_layout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button116_2 = QPushButton(self.dockWidgetContents_5)
        self.button116_2.setObjectName(u"button116_2")
        self.button116_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button116_2.sizePolicy().hasHeightForWidth())
        self.button116_2.setSizePolicy(sizePolicy)
        self.button116_2.setMinimumSize(QSize(28, 28))
        self.button116_2.setMaximumSize(QSize(28, 28))
        self.button116_2.setFont(font)

        self.button116_layout_2.addWidget(self.button116_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button116_layout_2, 4, 10, 1, 1)

        self.button16_2 = QPushButton(self.dockWidgetContents_5)
        self.button16_2.setObjectName(u"button16_2")
        sizePolicy.setHeightForWidth(self.button16_2.sizePolicy().hasHeightForWidth())
        self.button16_2.setSizePolicy(sizePolicy)
        self.button16_2.setMinimumSize(QSize(88, 44))
        self.button16_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button16_2, 5, 1, 1, 1)

        self.button12_2 = QPushButton(self.dockWidgetContents_5)
        self.button12_2.setObjectName(u"button12_2")
        sizePolicy.setHeightForWidth(self.button12_2.sizePolicy().hasHeightForWidth())
        self.button12_2.setSizePolicy(sizePolicy)
        self.button12_2.setMinimumSize(QSize(88, 44))
        self.button12_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button12_2, 6, 5, 1, 1)

        self.button10_2 = QPushButton(self.dockWidgetContents_5)
        self.button10_2.setObjectName(u"button10_2")
        sizePolicy.setHeightForWidth(self.button10_2.sizePolicy().hasHeightForWidth())
        self.button10_2.setSizePolicy(sizePolicy)
        self.button10_2.setMinimumSize(QSize(88, 44))
        self.button10_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button10_2, 6, 3, 1, 1)

        self.button49_2 = QPushButton(self.dockWidgetContents_5)
        self.button49_2.setObjectName(u"button49_2")
        sizePolicy.setHeightForWidth(self.button49_2.sizePolicy().hasHeightForWidth())
        self.button49_2.setSizePolicy(sizePolicy)
        self.button49_2.setMinimumSize(QSize(88, 44))
        self.button49_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button49_2, 1, 2, 1, 1)

        self.button30_2 = QPushButton(self.dockWidgetContents_5)
        self.button30_2.setObjectName(u"button30_2")
        sizePolicy.setHeightForWidth(self.button30_2.sizePolicy().hasHeightForWidth())
        self.button30_2.setSizePolicy(sizePolicy)
        self.button30_2.setMinimumSize(QSize(88, 44))
        self.button30_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button30_2, 4, 7, 1, 1)

        self.button113_layout_2 = QGridLayout()
        self.button113_layout_2.setObjectName(u"button113_layout_2")
        self.button113_layout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button113_2 = QPushButton(self.dockWidgetContents_5)
        self.button113_2.setObjectName(u"button113_2")
        self.button113_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button113_2.sizePolicy().hasHeightForWidth())
        self.button113_2.setSizePolicy(sizePolicy)
        self.button113_2.setMinimumSize(QSize(28, 28))
        self.button113_2.setMaximumSize(QSize(28, 28))
        self.button113_2.setFont(font)

        self.button113_layout_2.addWidget(self.button113_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button113_layout_2, 1, 10, 1, 1)

        self.button104_layout_2 = QGridLayout()
        self.button104_layout_2.setObjectName(u"button104_layout_2")
        self.button104_2 = QPushButton(self.dockWidgetContents_5)
        self.button104_2.setObjectName(u"button104_2")
        self.button104_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button104_2.sizePolicy().hasHeightForWidth())
        self.button104_2.setSizePolicy(sizePolicy)
        self.button104_2.setMinimumSize(QSize(28, 28))
        self.button104_2.setMaximumSize(QSize(28, 28))
        self.button104_2.setFont(font)

        self.button104_layout_2.addWidget(self.button104_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button104_layout_2, 8, 5, 1, 1)

        self.button25_2 = QPushButton(self.dockWidgetContents_5)
        self.button25_2.setObjectName(u"button25_2")
        sizePolicy.setHeightForWidth(self.button25_2.sizePolicy().hasHeightForWidth())
        self.button25_2.setSizePolicy(sizePolicy)
        self.button25_2.setMinimumSize(QSize(88, 44))
        self.button25_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button25_2, 4, 2, 1, 1)

        self.button63_2 = QPushButton(self.dockWidgetContents_5)
        self.button63_2.setObjectName(u"button63_2")
        sizePolicy.setHeightForWidth(self.button63_2.sizePolicy().hasHeightForWidth())
        self.button63_2.setSizePolicy(sizePolicy)
        self.button63_2.setMinimumSize(QSize(88, 44))
        self.button63_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button63_2, 0, 8, 1, 1)

        self.button122_layout_2 = QGridLayout()
        self.button122_layout_2.setObjectName(u"button122_layout_2")
        self.button122_layout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button122_2 = QPushButton(self.dockWidgetContents_5)
        self.button122_2.setObjectName(u"button122_2")
        self.button122_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button122_2.sizePolicy().hasHeightForWidth())
        self.button122_2.setSizePolicy(sizePolicy)
        self.button122_2.setMinimumSize(QSize(28, 28))
        self.button122_2.setMaximumSize(QSize(28, 28))
        self.button122_2.setFont(font)

        self.button122_layout_2.addWidget(self.button122_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button122_layout_2, 8, 10, 1, 1)

        self.button48_2 = QPushButton(self.dockWidgetContents_5)
        self.button48_2.setObjectName(u"button48_2")
        sizePolicy.setHeightForWidth(self.button48_2.sizePolicy().hasHeightForWidth())
        self.button48_2.setSizePolicy(sizePolicy)
        self.button48_2.setMinimumSize(QSize(88, 44))
        self.button48_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button48_2, 1, 1, 1, 1)

        self.button31_2 = QPushButton(self.dockWidgetContents_5)
        self.button31_2.setObjectName(u"button31_2")
        sizePolicy.setHeightForWidth(self.button31_2.sizePolicy().hasHeightForWidth())
        self.button31_2.setSizePolicy(sizePolicy)
        self.button31_2.setMinimumSize(QSize(88, 44))
        self.button31_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button31_2, 4, 8, 1, 1)

        self.button7_2 = QPushButton(self.dockWidgetContents_5)
        self.button7_2.setObjectName(u"button7_2")
        sizePolicy.setHeightForWidth(self.button7_2.sizePolicy().hasHeightForWidth())
        self.button7_2.setSizePolicy(sizePolicy)
        self.button7_2.setMinimumSize(QSize(88, 44))
        self.button7_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button7_2, 7, 8, 1, 1)

        self.button4_2 = QPushButton(self.dockWidgetContents_5)
        self.button4_2.setObjectName(u"button4_2")
        sizePolicy.setHeightForWidth(self.button4_2.sizePolicy().hasHeightForWidth())
        self.button4_2.setSizePolicy(sizePolicy)
        self.button4_2.setMinimumSize(QSize(88, 44))
        self.button4_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button4_2, 7, 5, 1, 1)

        self.button35_2 = QPushButton(self.dockWidgetContents_5)
        self.button35_2.setObjectName(u"button35_2")
        sizePolicy.setHeightForWidth(self.button35_2.sizePolicy().hasHeightForWidth())
        self.button35_2.setSizePolicy(sizePolicy)
        self.button35_2.setMinimumSize(QSize(88, 44))
        self.button35_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button35_2, 3, 4, 1, 1)

        self.button39_2 = QPushButton(self.dockWidgetContents_5)
        self.button39_2.setObjectName(u"button39_2")
        sizePolicy.setHeightForWidth(self.button39_2.sizePolicy().hasHeightForWidth())
        self.button39_2.setSizePolicy(sizePolicy)
        self.button39_2.setMinimumSize(QSize(88, 44))
        self.button39_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button39_2, 3, 8, 1, 1)

        self.button24_2 = QPushButton(self.dockWidgetContents_5)
        self.button24_2.setObjectName(u"button24_2")
        sizePolicy.setHeightForWidth(self.button24_2.sizePolicy().hasHeightForWidth())
        self.button24_2.setSizePolicy(sizePolicy)
        self.button24_2.setMinimumSize(QSize(88, 44))
        self.button24_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button24_2, 4, 1, 1, 1)

        self.button3_2 = QPushButton(self.dockWidgetContents_5)
        self.button3_2.setObjectName(u"button3_2")
        sizePolicy.setHeightForWidth(self.button3_2.sizePolicy().hasHeightForWidth())
        self.button3_2.setSizePolicy(sizePolicy)
        self.button3_2.setMinimumSize(QSize(88, 44))
        self.button3_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button3_2, 7, 4, 1, 1)

        self.button46_2 = QPushButton(self.dockWidgetContents_5)
        self.button46_2.setObjectName(u"button46_2")
        sizePolicy.setHeightForWidth(self.button46_2.sizePolicy().hasHeightForWidth())
        self.button46_2.setSizePolicy(sizePolicy)
        self.button46_2.setMinimumSize(QSize(88, 44))
        self.button46_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button46_2, 2, 7, 1, 1)

        self.button40_2 = QPushButton(self.dockWidgetContents_5)
        self.button40_2.setObjectName(u"button40_2")
        sizePolicy.setHeightForWidth(self.button40_2.sizePolicy().hasHeightForWidth())
        self.button40_2.setSizePolicy(sizePolicy)
        self.button40_2.setMinimumSize(QSize(88, 44))
        self.button40_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button40_2, 2, 1, 1, 1)

        self.button55_2 = QPushButton(self.dockWidgetContents_5)
        self.button55_2.setObjectName(u"button55_2")
        sizePolicy.setHeightForWidth(self.button55_2.sizePolicy().hasHeightForWidth())
        self.button55_2.setSizePolicy(sizePolicy)
        self.button55_2.setMinimumSize(QSize(88, 44))
        self.button55_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button55_2, 1, 8, 1, 1)

        self.button9_2 = QPushButton(self.dockWidgetContents_5)
        self.button9_2.setObjectName(u"button9_2")
        sizePolicy.setHeightForWidth(self.button9_2.sizePolicy().hasHeightForWidth())
        self.button9_2.setSizePolicy(sizePolicy)
        self.button9_2.setMinimumSize(QSize(88, 44))
        self.button9_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button9_2, 6, 2, 1, 1)

        self.button5_2 = QPushButton(self.dockWidgetContents_5)
        self.button5_2.setObjectName(u"button5_2")
        sizePolicy.setHeightForWidth(self.button5_2.sizePolicy().hasHeightForWidth())
        self.button5_2.setSizePolicy(sizePolicy)
        self.button5_2.setMinimumSize(QSize(88, 44))
        self.button5_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button5_2, 7, 6, 1, 1)

        self.button38_2 = QPushButton(self.dockWidgetContents_5)
        self.button38_2.setObjectName(u"button38_2")
        sizePolicy.setHeightForWidth(self.button38_2.sizePolicy().hasHeightForWidth())
        self.button38_2.setSizePolicy(sizePolicy)
        self.button38_2.setMinimumSize(QSize(88, 44))
        self.button38_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button38_2, 3, 7, 1, 1)

        self.button100_layout_2 = QGridLayout()
        self.button100_layout_2.setObjectName(u"button100_layout_2")
        self.button100_2 = QPushButton(self.dockWidgetContents_5)
        self.button100_2.setObjectName(u"button100_2")
        self.button100_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button100_2.sizePolicy().hasHeightForWidth())
        self.button100_2.setSizePolicy(sizePolicy)
        self.button100_2.setMinimumSize(QSize(28, 28))
        self.button100_2.setMaximumSize(QSize(28, 28))
        self.button100_2.setFont(font)
        self.button100_2.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.button100_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.button100_2.setAutoDefault(False)

        self.button100_layout_2.addWidget(self.button100_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button100_layout_2, 8, 1, 1, 1)

        self.button119_layout_2 = QGridLayout()
        self.button119_layout_2.setObjectName(u"button119_layout_2")
        self.button119_layout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button119_2 = QPushButton(self.dockWidgetContents_5)
        self.button119_2.setObjectName(u"button119_2")
        self.button119_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button119_2.sizePolicy().hasHeightForWidth())
        self.button119_2.setSizePolicy(sizePolicy)
        self.button119_2.setMinimumSize(QSize(28, 28))
        self.button119_2.setMaximumSize(QSize(28, 28))
        self.button119_2.setFont(font)

        self.button119_layout_2.addWidget(self.button119_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button119_layout_2, 7, 10, 1, 1)

        self.button52_2 = QPushButton(self.dockWidgetContents_5)
        self.button52_2.setObjectName(u"button52_2")
        sizePolicy.setHeightForWidth(self.button52_2.sizePolicy().hasHeightForWidth())
        self.button52_2.setSizePolicy(sizePolicy)
        self.button52_2.setMinimumSize(QSize(88, 44))
        self.button52_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button52_2, 1, 5, 1, 1)

        self.button51_2 = QPushButton(self.dockWidgetContents_5)
        self.button51_2.setObjectName(u"button51_2")
        sizePolicy.setHeightForWidth(self.button51_2.sizePolicy().hasHeightForWidth())
        self.button51_2.setSizePolicy(sizePolicy)
        self.button51_2.setMinimumSize(QSize(88, 44))
        self.button51_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button51_2, 1, 4, 1, 1)

        self.button60_2 = QPushButton(self.dockWidgetContents_5)
        self.button60_2.setObjectName(u"button60_2")
        sizePolicy.setHeightForWidth(self.button60_2.sizePolicy().hasHeightForWidth())
        self.button60_2.setSizePolicy(sizePolicy)
        self.button60_2.setMinimumSize(QSize(88, 44))
        self.button60_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button60_2, 0, 5, 1, 1)

        self.button13_2 = QPushButton(self.dockWidgetContents_5)
        self.button13_2.setObjectName(u"button13_2")
        sizePolicy.setHeightForWidth(self.button13_2.sizePolicy().hasHeightForWidth())
        self.button13_2.setSizePolicy(sizePolicy)
        self.button13_2.setMinimumSize(QSize(88, 44))
        self.button13_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button13_2, 6, 6, 1, 1)

        self.button14_2 = QPushButton(self.dockWidgetContents_5)
        self.button14_2.setObjectName(u"button14_2")
        sizePolicy.setHeightForWidth(self.button14_2.sizePolicy().hasHeightForWidth())
        self.button14_2.setSizePolicy(sizePolicy)
        self.button14_2.setMinimumSize(QSize(88, 44))
        self.button14_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button14_2, 6, 7, 1, 1)

        self.button6_2 = QPushButton(self.dockWidgetContents_5)
        self.button6_2.setObjectName(u"button6_2")
        sizePolicy.setHeightForWidth(self.button6_2.sizePolicy().hasHeightForWidth())
        self.button6_2.setSizePolicy(sizePolicy)
        self.button6_2.setMinimumSize(QSize(88, 44))
        self.button6_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button6_2, 7, 7, 1, 1)

        self.button26_2 = QPushButton(self.dockWidgetContents_5)
        self.button26_2.setObjectName(u"button26_2")
        sizePolicy.setHeightForWidth(self.button26_2.sizePolicy().hasHeightForWidth())
        self.button26_2.setSizePolicy(sizePolicy)
        self.button26_2.setMinimumSize(QSize(88, 44))
        self.button26_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button26_2, 4, 3, 1, 1)

        self.button1_2 = QPushButton(self.dockWidgetContents_5)
        self.button1_2.setObjectName(u"button1_2")
        sizePolicy.setHeightForWidth(self.button1_2.sizePolicy().hasHeightForWidth())
        self.button1_2.setSizePolicy(sizePolicy)
        self.button1_2.setMinimumSize(QSize(88, 44))
        self.button1_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button1_2, 7, 2, 1, 1)

        self.button34_2 = QPushButton(self.dockWidgetContents_5)
        self.button34_2.setObjectName(u"button34_2")
        sizePolicy.setHeightForWidth(self.button34_2.sizePolicy().hasHeightForWidth())
        self.button34_2.setSizePolicy(sizePolicy)
        self.button34_2.setMinimumSize(QSize(88, 44))
        self.button34_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button34_2, 3, 3, 1, 1)

        self.button117_layout_2 = QGridLayout()
        self.button117_layout_2.setObjectName(u"button117_layout_2")
        self.button117_layout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button117_2 = QPushButton(self.dockWidgetContents_5)
        self.button117_2.setObjectName(u"button117_2")
        self.button117_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button117_2.sizePolicy().hasHeightForWidth())
        self.button117_2.setSizePolicy(sizePolicy)
        self.button117_2.setMinimumSize(QSize(28, 28))
        self.button117_2.setMaximumSize(QSize(28, 28))
        self.button117_2.setFont(font)

        self.button117_layout_2.addWidget(self.button117_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button117_layout_2, 5, 10, 1, 1)

        self.button115_layout_2 = QGridLayout()
        self.button115_layout_2.setObjectName(u"button115_layout_2")
        self.button115_layout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button115_2 = QPushButton(self.dockWidgetContents_5)
        self.button115_2.setObjectName(u"button115_2")
        self.button115_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button115_2.sizePolicy().hasHeightForWidth())
        self.button115_2.setSizePolicy(sizePolicy)
        self.button115_2.setMinimumSize(QSize(28, 28))
        self.button115_2.setMaximumSize(QSize(28, 28))
        self.button115_2.setFont(font)

        self.button115_layout_2.addWidget(self.button115_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button115_layout_2, 3, 10, 1, 1)

        self.button62_2 = QPushButton(self.dockWidgetContents_5)
        self.button62_2.setObjectName(u"button62_2")
        sizePolicy.setHeightForWidth(self.button62_2.sizePolicy().hasHeightForWidth())
        self.button62_2.setSizePolicy(sizePolicy)
        self.button62_2.setMinimumSize(QSize(88, 44))
        self.button62_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button62_2, 0, 7, 1, 1)

        self.button58_2 = QPushButton(self.dockWidgetContents_5)
        self.button58_2.setObjectName(u"button58_2")
        sizePolicy.setHeightForWidth(self.button58_2.sizePolicy().hasHeightForWidth())
        self.button58_2.setSizePolicy(sizePolicy)
        self.button58_2.setMinimumSize(QSize(88, 44))
        self.button58_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button58_2, 0, 3, 1, 1)

        self.button29_2 = QPushButton(self.dockWidgetContents_5)
        self.button29_2.setObjectName(u"button29_2")
        sizePolicy.setHeightForWidth(self.button29_2.sizePolicy().hasHeightForWidth())
        self.button29_2.setSizePolicy(sizePolicy)
        self.button29_2.setMinimumSize(QSize(88, 44))
        self.button29_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button29_2, 4, 6, 1, 1)

        self.button21_2 = QPushButton(self.dockWidgetContents_5)
        self.button21_2.setObjectName(u"button21_2")
        sizePolicy.setHeightForWidth(self.button21_2.sizePolicy().hasHeightForWidth())
        self.button21_2.setSizePolicy(sizePolicy)
        self.button21_2.setMinimumSize(QSize(88, 44))
        self.button21_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button21_2, 5, 6, 1, 1)

        self.button43_2 = QPushButton(self.dockWidgetContents_5)
        self.button43_2.setObjectName(u"button43_2")
        sizePolicy.setHeightForWidth(self.button43_2.sizePolicy().hasHeightForWidth())
        self.button43_2.setSizePolicy(sizePolicy)
        self.button43_2.setMinimumSize(QSize(88, 44))
        self.button43_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button43_2, 2, 4, 1, 1)

        self.button15_2 = QPushButton(self.dockWidgetContents_5)
        self.button15_2.setObjectName(u"button15_2")
        sizePolicy.setHeightForWidth(self.button15_2.sizePolicy().hasHeightForWidth())
        self.button15_2.setSizePolicy(sizePolicy)
        self.button15_2.setMinimumSize(QSize(88, 44))
        self.button15_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button15_2, 6, 8, 1, 1)

        self.right_padding2_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.right_padding2_2, 7, 11, 1, 1)

        self.button32_2 = QPushButton(self.dockWidgetContents_5)
        self.button32_2.setObjectName(u"button32_2")
        sizePolicy.setHeightForWidth(self.button32_2.sizePolicy().hasHeightForWidth())
        self.button32_2.setSizePolicy(sizePolicy)
        self.button32_2.setMinimumSize(QSize(88, 44))
        self.button32_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button32_2, 3, 1, 1, 1)

        self.button59_2 = QPushButton(self.dockWidgetContents_5)
        self.button59_2.setObjectName(u"button59_2")
        sizePolicy.setHeightForWidth(self.button59_2.sizePolicy().hasHeightForWidth())
        self.button59_2.setSizePolicy(sizePolicy)
        self.button59_2.setMinimumSize(QSize(88, 44))
        self.button59_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button59_2, 0, 4, 1, 1)

        self.button118_layout_2 = QGridLayout()
        self.button118_layout_2.setObjectName(u"button118_layout_2")
        self.button118_layout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button118_2 = QPushButton(self.dockWidgetContents_5)
        self.button118_2.setObjectName(u"button118_2")
        self.button118_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button118_2.sizePolicy().hasHeightForWidth())
        self.button118_2.setSizePolicy(sizePolicy)
        self.button118_2.setMinimumSize(QSize(28, 28))
        self.button118_2.setMaximumSize(QSize(28, 28))
        self.button118_2.setFont(font)

        self.button118_layout_2.addWidget(self.button118_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button118_layout_2, 6, 10, 1, 1)

        self.button22_2 = QPushButton(self.dockWidgetContents_5)
        self.button22_2.setObjectName(u"button22_2")
        sizePolicy.setHeightForWidth(self.button22_2.sizePolicy().hasHeightForWidth())
        self.button22_2.setSizePolicy(sizePolicy)
        self.button22_2.setMinimumSize(QSize(88, 44))
        self.button22_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button22_2, 5, 7, 1, 1)

        self.button42_2 = QPushButton(self.dockWidgetContents_5)
        self.button42_2.setObjectName(u"button42_2")
        sizePolicy.setHeightForWidth(self.button42_2.sizePolicy().hasHeightForWidth())
        self.button42_2.setSizePolicy(sizePolicy)
        self.button42_2.setMinimumSize(QSize(88, 44))
        self.button42_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button42_2, 2, 3, 1, 1)

        self.button107_layout_2 = QGridLayout()
        self.button107_layout_2.setObjectName(u"button107_layout_2")
        self.button107_2 = QPushButton(self.dockWidgetContents_5)
        self.button107_2.setObjectName(u"button107_2")
        self.button107_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button107_2.sizePolicy().hasHeightForWidth())
        self.button107_2.setSizePolicy(sizePolicy)
        self.button107_2.setMinimumSize(QSize(28, 28))
        self.button107_2.setMaximumSize(QSize(28, 28))
        self.button107_2.setFont(font)

        self.button107_layout_2.addWidget(self.button107_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button107_layout_2, 8, 8, 1, 1)

        self.right_padding_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.right_padding_2, 8, 11, 1, 1)

        self.button27_2 = QPushButton(self.dockWidgetContents_5)
        self.button27_2.setObjectName(u"button27_2")
        sizePolicy.setHeightForWidth(self.button27_2.sizePolicy().hasHeightForWidth())
        self.button27_2.setSizePolicy(sizePolicy)
        self.button27_2.setMinimumSize(QSize(88, 44))
        self.button27_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button27_2, 4, 4, 1, 1)

        self.frame_fader52_2 = QFrame(self.dockWidgetContents_5)
        self.frame_fader52_2.setObjectName(u"frame_fader52_2")
        self.frame_fader52_2.setMinimumSize(QSize(88, 250))
        self.frame_fader52_2.setMaximumSize(QSize(88, 250))
        self.frame_fader52_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader52_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_fader52_2)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader52_2 = QGridLayout()
        self.below_button_layout_fader52_2.setSpacing(0)
        self.below_button_layout_fader52_2.setObjectName(u"below_button_layout_fader52_2")
        self.pushButton_fader52_2 = QPushButton(self.frame_fader52_2)
        self.pushButton_fader52_2.setObjectName(u"pushButton_fader52_2")

        self.below_button_layout_fader52_2.addWidget(self.pushButton_fader52_2, 2, 0, 1, 1)

        self.fader52_layout_2 = QGridLayout()
        self.fader52_layout_2.setObjectName(u"fader52_layout_2")
        self.fader52_2 = QSlider(self.frame_fader52_2)
        self.fader52_2.setObjectName(u"fader52_2")
        sizePolicy.setHeightForWidth(self.fader52_2.sizePolicy().hasHeightForWidth())
        self.fader52_2.setSizePolicy(sizePolicy)
        self.fader52_2.setMinimumSize(QSize(0, 190))
        self.fader52_2.setMaximumSize(QSize(15, 190))
        self.fader52_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader52_2.setAutoFillBackground(False)
        self.fader52_2.setMaximum(127)
        self.fader52_2.setSliderPosition(0)
        self.fader52_2.setOrientation(Qt.Orientation.Vertical)
        self.fader52_2.setInvertedAppearance(False)
        self.fader52_2.setInvertedControls(False)

        self.fader52_layout_2.addWidget(self.fader52_2, 0, 0, 1, 1)


        self.below_button_layout_fader52_2.addLayout(self.fader52_layout_2, 0, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader52_2.addItem(self.verticalSpacer_15, 1, 0, 1, 1)


        self.gridLayout_19.addLayout(self.below_button_layout_fader52_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_fader52_2, 10, 5, 1, 1)

        self.button17_2 = QPushButton(self.dockWidgetContents_5)
        self.button17_2.setObjectName(u"button17_2")
        sizePolicy.setHeightForWidth(self.button17_2.sizePolicy().hasHeightForWidth())
        self.button17_2.setSizePolicy(sizePolicy)
        self.button17_2.setMinimumSize(QSize(88, 44))
        self.button17_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button17_2, 5, 2, 1, 1)

        self.frame_fader53_2 = QFrame(self.dockWidgetContents_5)
        self.frame_fader53_2.setObjectName(u"frame_fader53_2")
        self.frame_fader53_2.setMinimumSize(QSize(88, 250))
        self.frame_fader53_2.setMaximumSize(QSize(88, 250))
        self.frame_fader53_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader53_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_fader53_2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader53_2 = QGridLayout()
        self.below_button_layout_fader53_2.setSpacing(0)
        self.below_button_layout_fader53_2.setObjectName(u"below_button_layout_fader53_2")
        self.pushButton_fader53_2 = QPushButton(self.frame_fader53_2)
        self.pushButton_fader53_2.setObjectName(u"pushButton_fader53_2")

        self.below_button_layout_fader53_2.addWidget(self.pushButton_fader53_2, 2, 0, 1, 1)

        self.fader53_layout_2 = QGridLayout()
        self.fader53_layout_2.setObjectName(u"fader53_layout_2")
        self.fader53_2 = QSlider(self.frame_fader53_2)
        self.fader53_2.setObjectName(u"fader53_2")
        sizePolicy.setHeightForWidth(self.fader53_2.sizePolicy().hasHeightForWidth())
        self.fader53_2.setSizePolicy(sizePolicy)
        self.fader53_2.setMinimumSize(QSize(0, 190))
        self.fader53_2.setMaximumSize(QSize(15, 190))
        self.fader53_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader53_2.setAutoFillBackground(False)
        self.fader53_2.setMaximum(127)
        self.fader53_2.setSliderPosition(0)
        self.fader53_2.setOrientation(Qt.Orientation.Vertical)
        self.fader53_2.setInvertedAppearance(False)
        self.fader53_2.setInvertedControls(False)

        self.fader53_layout_2.addWidget(self.fader53_2, 0, 0, 1, 1)


        self.below_button_layout_fader53_2.addLayout(self.fader53_layout_2, 0, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader53_2.addItem(self.verticalSpacer_13, 1, 0, 1, 1)


        self.gridLayout_23.addLayout(self.below_button_layout_fader53_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_fader53_2, 10, 6, 1, 1)

        self.frame_fader49_2 = QFrame(self.dockWidgetContents_5)
        self.frame_fader49_2.setObjectName(u"frame_fader49_2")
        self.frame_fader49_2.setMinimumSize(QSize(88, 250))
        self.frame_fader49_2.setMaximumSize(QSize(88, 250))
        self.frame_fader49_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader49_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_fader49_2)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader49_2 = QGridLayout()
        self.below_button_layout_fader49_2.setSpacing(0)
        self.below_button_layout_fader49_2.setObjectName(u"below_button_layout_fader49_2")
        self.fader49_layout_2 = QGridLayout()
        self.fader49_layout_2.setObjectName(u"fader49_layout_2")
        self.fader49_2 = QSlider(self.frame_fader49_2)
        self.fader49_2.setObjectName(u"fader49_2")
        sizePolicy.setHeightForWidth(self.fader49_2.sizePolicy().hasHeightForWidth())
        self.fader49_2.setSizePolicy(sizePolicy)
        self.fader49_2.setMinimumSize(QSize(0, 190))
        self.fader49_2.setMaximumSize(QSize(15, 190))
        self.fader49_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader49_2.setAutoFillBackground(False)
        self.fader49_2.setMaximum(127)
        self.fader49_2.setSliderPosition(0)
        self.fader49_2.setOrientation(Qt.Orientation.Vertical)
        self.fader49_2.setInvertedAppearance(False)
        self.fader49_2.setInvertedControls(False)

        self.fader49_layout_2.addWidget(self.fader49_2, 0, 0, 1, 1)


        self.below_button_layout_fader49_2.addLayout(self.fader49_layout_2, 0, 0, 1, 1)

        self.pushButton_fader49_2 = QPushButton(self.frame_fader49_2)
        self.pushButton_fader49_2.setObjectName(u"pushButton_fader49_2")

        self.below_button_layout_fader49_2.addWidget(self.pushButton_fader49_2, 2, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader49_2.addItem(self.verticalSpacer_18, 1, 0, 1, 1)


        self.gridLayout_24.addLayout(self.below_button_layout_fader49_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_fader49_2, 10, 2, 1, 1)

        self.button37_2 = QPushButton(self.dockWidgetContents_5)
        self.button37_2.setObjectName(u"button37_2")
        sizePolicy.setHeightForWidth(self.button37_2.sizePolicy().hasHeightForWidth())
        self.button37_2.setSizePolicy(sizePolicy)
        self.button37_2.setMinimumSize(QSize(88, 44))
        self.button37_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button37_2, 3, 6, 1, 1)

        self.button41_2 = QPushButton(self.dockWidgetContents_5)
        self.button41_2.setObjectName(u"button41_2")
        sizePolicy.setHeightForWidth(self.button41_2.sizePolicy().hasHeightForWidth())
        self.button41_2.setSizePolicy(sizePolicy)
        self.button41_2.setMinimumSize(QSize(88, 44))
        self.button41_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button41_2, 2, 2, 1, 1)

        self.button0_2 = QPushButton(self.dockWidgetContents_5)
        self.button0_2.setObjectName(u"button0_2")
        sizePolicy.setHeightForWidth(self.button0_2.sizePolicy().hasHeightForWidth())
        self.button0_2.setSizePolicy(sizePolicy)
        self.button0_2.setMinimumSize(QSize(88, 44))
        self.button0_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button0_2, 7, 1, 1, 1)

        self.left_padding_3 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.left_padding_3, 7, 0, 1, 1)

        self.button56_2 = QPushButton(self.dockWidgetContents_5)
        self.button56_2.setObjectName(u"button56_2")
        sizePolicy.setHeightForWidth(self.button56_2.sizePolicy().hasHeightForWidth())
        self.button56_2.setSizePolicy(sizePolicy)
        self.button56_2.setMinimumSize(QSize(88, 44))
        self.button56_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button56_2, 0, 1, 1, 1)

        self.button23_2 = QPushButton(self.dockWidgetContents_5)
        self.button23_2.setObjectName(u"button23_2")
        sizePolicy.setHeightForWidth(self.button23_2.sizePolicy().hasHeightForWidth())
        self.button23_2.setSizePolicy(sizePolicy)
        self.button23_2.setMinimumSize(QSize(88, 44))
        self.button23_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button23_2, 5, 8, 1, 1)

        self.button54_2 = QPushButton(self.dockWidgetContents_5)
        self.button54_2.setObjectName(u"button54_2")
        sizePolicy.setHeightForWidth(self.button54_2.sizePolicy().hasHeightForWidth())
        self.button54_2.setSizePolicy(sizePolicy)
        self.button54_2.setMinimumSize(QSize(88, 44))
        self.button54_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button54_2, 1, 7, 1, 1)

        self.frame_fader48_2 = QFrame(self.dockWidgetContents_5)
        self.frame_fader48_2.setObjectName(u"frame_fader48_2")
        self.frame_fader48_2.setMinimumSize(QSize(88, 250))
        self.frame_fader48_2.setMaximumSize(QSize(88, 250))
        self.frame_fader48_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader48_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_fader48_2)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader48_2 = QGridLayout()
        self.below_button_layout_fader48_2.setSpacing(0)
        self.below_button_layout_fader48_2.setObjectName(u"below_button_layout_fader48_2")
        self.fader48_layout_2 = QGridLayout()
        self.fader48_layout_2.setObjectName(u"fader48_layout_2")
        self.fader48_2 = QSlider(self.frame_fader48_2)
        self.fader48_2.setObjectName(u"fader48_2")
        sizePolicy.setHeightForWidth(self.fader48_2.sizePolicy().hasHeightForWidth())
        self.fader48_2.setSizePolicy(sizePolicy)
        self.fader48_2.setMinimumSize(QSize(0, 190))
        self.fader48_2.setMaximumSize(QSize(15, 190))
        self.fader48_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader48_2.setAutoFillBackground(False)
        self.fader48_2.setMaximum(127)
        self.fader48_2.setSliderPosition(0)
        self.fader48_2.setOrientation(Qt.Orientation.Vertical)
        self.fader48_2.setInvertedAppearance(False)
        self.fader48_2.setInvertedControls(False)

        self.fader48_layout_2.addWidget(self.fader48_2, 0, 0, 1, 1)


        self.below_button_layout_fader48_2.addLayout(self.fader48_layout_2, 0, 0, 1, 1)

        self.pushButton_fader48_2 = QPushButton(self.frame_fader48_2)
        self.pushButton_fader48_2.setObjectName(u"pushButton_fader48_2")

        self.below_button_layout_fader48_2.addWidget(self.pushButton_fader48_2, 2, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader48_2.addItem(self.verticalSpacer_17, 1, 0, 1, 1)


        self.gridLayout_25.addLayout(self.below_button_layout_fader48_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_fader48_2, 10, 1, 1, 1)

        self.button106_layout_2 = QGridLayout()
        self.button106_layout_2.setObjectName(u"button106_layout_2")
        self.button106_2 = QPushButton(self.dockWidgetContents_5)
        self.button106_2.setObjectName(u"button106_2")
        self.button106_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button106_2.sizePolicy().hasHeightForWidth())
        self.button106_2.setSizePolicy(sizePolicy)
        self.button106_2.setMinimumSize(QSize(28, 28))
        self.button106_2.setMaximumSize(QSize(28, 28))
        self.button106_2.setFont(font)

        self.button106_layout_2.addWidget(self.button106_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button106_layout_2, 8, 7, 1, 1)

        self.button33_2 = QPushButton(self.dockWidgetContents_5)
        self.button33_2.setObjectName(u"button33_2")
        sizePolicy.setHeightForWidth(self.button33_2.sizePolicy().hasHeightForWidth())
        self.button33_2.setSizePolicy(sizePolicy)
        self.button33_2.setMinimumSize(QSize(88, 44))
        self.button33_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button33_2, 3, 2, 1, 1)

        self.button28_2 = QPushButton(self.dockWidgetContents_5)
        self.button28_2.setObjectName(u"button28_2")
        sizePolicy.setHeightForWidth(self.button28_2.sizePolicy().hasHeightForWidth())
        self.button28_2.setSizePolicy(sizePolicy)
        self.button28_2.setMinimumSize(QSize(88, 44))
        self.button28_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button28_2, 4, 5, 1, 1)

        self.button2_2 = QPushButton(self.dockWidgetContents_5)
        self.button2_2.setObjectName(u"button2_2")
        sizePolicy.setHeightForWidth(self.button2_2.sizePolicy().hasHeightForWidth())
        self.button2_2.setSizePolicy(sizePolicy)
        self.button2_2.setMinimumSize(QSize(88, 44))
        self.button2_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button2_2, 7, 3, 1, 1)

        self.button11_2 = QPushButton(self.dockWidgetContents_5)
        self.button11_2.setObjectName(u"button11_2")
        sizePolicy.setHeightForWidth(self.button11_2.sizePolicy().hasHeightForWidth())
        self.button11_2.setSizePolicy(sizePolicy)
        self.button11_2.setMinimumSize(QSize(88, 44))
        self.button11_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button11_2, 6, 4, 1, 1)

        self.button102_layout_2 = QGridLayout()
        self.button102_layout_2.setObjectName(u"button102_layout_2")
        self.button102_2 = QPushButton(self.dockWidgetContents_5)
        self.button102_2.setObjectName(u"button102_2")
        self.button102_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button102_2.sizePolicy().hasHeightForWidth())
        self.button102_2.setSizePolicy(sizePolicy)
        self.button102_2.setMinimumSize(QSize(28, 28))
        self.button102_2.setMaximumSize(QSize(28, 28))
        self.button102_2.setFont(font)

        self.button102_layout_2.addWidget(self.button102_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button102_layout_2, 8, 3, 1, 1)

        self.button18_2 = QPushButton(self.dockWidgetContents_5)
        self.button18_2.setObjectName(u"button18_2")
        sizePolicy.setHeightForWidth(self.button18_2.sizePolicy().hasHeightForWidth())
        self.button18_2.setSizePolicy(sizePolicy)
        self.button18_2.setMinimumSize(QSize(88, 44))
        self.button18_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button18_2, 5, 3, 1, 1)

        self.button19_2 = QPushButton(self.dockWidgetContents_5)
        self.button19_2.setObjectName(u"button19_2")
        sizePolicy.setHeightForWidth(self.button19_2.sizePolicy().hasHeightForWidth())
        self.button19_2.setSizePolicy(sizePolicy)
        self.button19_2.setMinimumSize(QSize(88, 44))
        self.button19_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button19_2, 5, 4, 1, 1)

        self.button47_2 = QPushButton(self.dockWidgetContents_5)
        self.button47_2.setObjectName(u"button47_2")
        sizePolicy.setHeightForWidth(self.button47_2.sizePolicy().hasHeightForWidth())
        self.button47_2.setSizePolicy(sizePolicy)
        self.button47_2.setMinimumSize(QSize(88, 44))
        self.button47_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button47_2, 2, 8, 1, 1)

        self.button53_2 = QPushButton(self.dockWidgetContents_5)
        self.button53_2.setObjectName(u"button53_2")
        sizePolicy.setHeightForWidth(self.button53_2.sizePolicy().hasHeightForWidth())
        self.button53_2.setSizePolicy(sizePolicy)
        self.button53_2.setMinimumSize(QSize(88, 44))
        self.button53_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button53_2, 1, 6, 1, 1)

        self.button112_layout_2 = QGridLayout()
        self.button112_layout_2.setObjectName(u"button112_layout_2")
        self.button112_layout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button112_2 = QPushButton(self.dockWidgetContents_5)
        self.button112_2.setObjectName(u"button112_2")
        self.button112_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button112_2.sizePolicy().hasHeightForWidth())
        self.button112_2.setSizePolicy(sizePolicy)
        self.button112_2.setMinimumSize(QSize(28, 28))
        self.button112_2.setMaximumSize(QSize(28, 28))
        self.button112_2.setFont(font)

        self.button112_layout_2.addWidget(self.button112_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button112_layout_2, 0, 10, 1, 1)

        self.button114_layout_2 = QGridLayout()
        self.button114_layout_2.setObjectName(u"button114_layout_2")
        self.button114_layout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button114_2 = QPushButton(self.dockWidgetContents_5)
        self.button114_2.setObjectName(u"button114_2")
        self.button114_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button114_2.sizePolicy().hasHeightForWidth())
        self.button114_2.setSizePolicy(sizePolicy)
        self.button114_2.setMinimumSize(QSize(28, 28))
        self.button114_2.setMaximumSize(QSize(28, 28))
        self.button114_2.setFont(font)

        self.button114_layout_2.addWidget(self.button114_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button114_layout_2, 2, 10, 1, 1)

        self.button50_2 = QPushButton(self.dockWidgetContents_5)
        self.button50_2.setObjectName(u"button50_2")
        sizePolicy.setHeightForWidth(self.button50_2.sizePolicy().hasHeightForWidth())
        self.button50_2.setSizePolicy(sizePolicy)
        self.button50_2.setMinimumSize(QSize(88, 44))
        self.button50_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button50_2, 1, 3, 1, 1)

        self.left_padding_4 = QSpacerItem(0, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.left_padding_4, 8, 0, 1, 1)

        self.frame_fader51_2 = QFrame(self.dockWidgetContents_5)
        self.frame_fader51_2.setObjectName(u"frame_fader51_2")
        self.frame_fader51_2.setMinimumSize(QSize(88, 250))
        self.frame_fader51_2.setMaximumSize(QSize(88, 250))
        self.frame_fader51_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader51_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_fader51_2)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader51_2 = QGridLayout()
        self.below_button_layout_fader51_2.setSpacing(0)
        self.below_button_layout_fader51_2.setObjectName(u"below_button_layout_fader51_2")
        self.pushButton_fader51_2 = QPushButton(self.frame_fader51_2)
        self.pushButton_fader51_2.setObjectName(u"pushButton_fader51_2")

        self.below_button_layout_fader51_2.addWidget(self.pushButton_fader51_2, 2, 0, 1, 1)

        self.fader51_layout_2 = QGridLayout()
        self.fader51_layout_2.setObjectName(u"fader51_layout_2")
        self.fader51_2 = QSlider(self.frame_fader51_2)
        self.fader51_2.setObjectName(u"fader51_2")
        sizePolicy.setHeightForWidth(self.fader51_2.sizePolicy().hasHeightForWidth())
        self.fader51_2.setSizePolicy(sizePolicy)
        self.fader51_2.setMinimumSize(QSize(0, 190))
        self.fader51_2.setMaximumSize(QSize(15, 190))
        self.fader51_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader51_2.setAutoFillBackground(False)
        self.fader51_2.setMaximum(127)
        self.fader51_2.setSliderPosition(0)
        self.fader51_2.setOrientation(Qt.Orientation.Vertical)
        self.fader51_2.setInvertedAppearance(False)
        self.fader51_2.setInvertedControls(False)

        self.fader51_layout_2.addWidget(self.fader51_2, 0, 0, 1, 1)


        self.below_button_layout_fader51_2.addLayout(self.fader51_layout_2, 0, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader51_2.addItem(self.verticalSpacer_14, 1, 0, 1, 1)


        self.gridLayout_26.addLayout(self.below_button_layout_fader51_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_fader51_2, 10, 4, 1, 1)

        self.frame_fader50_2 = QFrame(self.dockWidgetContents_5)
        self.frame_fader50_2.setObjectName(u"frame_fader50_2")
        self.frame_fader50_2.setMinimumSize(QSize(88, 250))
        self.frame_fader50_2.setMaximumSize(QSize(88, 250))
        self.frame_fader50_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader50_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_fader50_2)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader50_2 = QGridLayout()
        self.below_button_layout_fader50_2.setSpacing(0)
        self.below_button_layout_fader50_2.setObjectName(u"below_button_layout_fader50_2")
        self.pushButton_fader50_2 = QPushButton(self.frame_fader50_2)
        self.pushButton_fader50_2.setObjectName(u"pushButton_fader50_2")

        self.below_button_layout_fader50_2.addWidget(self.pushButton_fader50_2, 2, 0, 1, 1)

        self.fader50_layout_2 = QGridLayout()
        self.fader50_layout_2.setObjectName(u"fader50_layout_2")
        self.fader50_2 = QSlider(self.frame_fader50_2)
        self.fader50_2.setObjectName(u"fader50_2")
        sizePolicy.setHeightForWidth(self.fader50_2.sizePolicy().hasHeightForWidth())
        self.fader50_2.setSizePolicy(sizePolicy)
        self.fader50_2.setMinimumSize(QSize(0, 190))
        self.fader50_2.setMaximumSize(QSize(15, 190))
        self.fader50_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader50_2.setAutoFillBackground(False)
        self.fader50_2.setMaximum(127)
        self.fader50_2.setSliderPosition(0)
        self.fader50_2.setOrientation(Qt.Orientation.Vertical)
        self.fader50_2.setInvertedAppearance(False)
        self.fader50_2.setInvertedControls(False)

        self.fader50_layout_2.addWidget(self.fader50_2, 0, 0, 1, 1)


        self.below_button_layout_fader50_2.addLayout(self.fader50_layout_2, 0, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader50_2.addItem(self.verticalSpacer_16, 1, 0, 1, 1)


        self.gridLayout_27.addLayout(self.below_button_layout_fader50_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_fader50_2, 10, 3, 1, 1)

        self.button105_layout_2 = QGridLayout()
        self.button105_layout_2.setObjectName(u"button105_layout_2")
        self.button105_2 = QPushButton(self.dockWidgetContents_5)
        self.button105_2.setObjectName(u"button105_2")
        self.button105_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button105_2.sizePolicy().hasHeightForWidth())
        self.button105_2.setSizePolicy(sizePolicy)
        self.button105_2.setMinimumSize(QSize(28, 28))
        self.button105_2.setMaximumSize(QSize(28, 28))
        self.button105_2.setFont(font)

        self.button105_layout_2.addWidget(self.button105_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button105_layout_2, 8, 6, 1, 1)

        self.button20_2 = QPushButton(self.dockWidgetContents_5)
        self.button20_2.setObjectName(u"button20_2")
        sizePolicy.setHeightForWidth(self.button20_2.sizePolicy().hasHeightForWidth())
        self.button20_2.setSizePolicy(sizePolicy)
        self.button20_2.setMinimumSize(QSize(88, 44))
        self.button20_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button20_2, 5, 5, 1, 1)

        self.button101_layout_2 = QGridLayout()
        self.button101_layout_2.setObjectName(u"button101_layout_2")
        self.button101_2 = QPushButton(self.dockWidgetContents_5)
        self.button101_2.setObjectName(u"button101_2")
        self.button101_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button101_2.sizePolicy().hasHeightForWidth())
        self.button101_2.setSizePolicy(sizePolicy)
        self.button101_2.setMinimumSize(QSize(28, 28))
        self.button101_2.setMaximumSize(QSize(28, 28))
        self.button101_2.setFont(font)

        self.button101_layout_2.addWidget(self.button101_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button101_layout_2, 8, 2, 1, 1)

        self.button103_layout_2 = QGridLayout()
        self.button103_layout_2.setObjectName(u"button103_layout_2")
        self.button103_2 = QPushButton(self.dockWidgetContents_5)
        self.button103_2.setObjectName(u"button103_2")
        self.button103_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button103_2.sizePolicy().hasHeightForWidth())
        self.button103_2.setSizePolicy(sizePolicy)
        self.button103_2.setMinimumSize(QSize(28, 28))
        self.button103_2.setMaximumSize(QSize(28, 28))
        self.button103_2.setFont(font)

        self.button103_layout_2.addWidget(self.button103_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.button103_layout_2, 8, 4, 1, 1)

        self.button57_2 = QPushButton(self.dockWidgetContents_5)
        self.button57_2.setObjectName(u"button57_2")
        sizePolicy.setHeightForWidth(self.button57_2.sizePolicy().hasHeightForWidth())
        self.button57_2.setSizePolicy(sizePolicy)
        self.button57_2.setMinimumSize(QSize(88, 44))
        self.button57_2.setMaximumSize(QSize(88, 44))

        self.gridLayout_3.addWidget(self.button57_2, 0, 2, 1, 1)

        self.frame_fader54_2 = QFrame(self.dockWidgetContents_5)
        self.frame_fader54_2.setObjectName(u"frame_fader54_2")
        self.frame_fader54_2.setMinimumSize(QSize(88, 250))
        self.frame_fader54_2.setMaximumSize(QSize(88, 250))
        self.frame_fader54_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader54_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_fader54_2)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader54_2 = QGridLayout()
        self.below_button_layout_fader54_2.setSpacing(0)
        self.below_button_layout_fader54_2.setObjectName(u"below_button_layout_fader54_2")
        self.fader54_layout_2 = QGridLayout()
        self.fader54_layout_2.setObjectName(u"fader54_layout_2")
        self.fader54_2 = QSlider(self.frame_fader54_2)
        self.fader54_2.setObjectName(u"fader54_2")
        sizePolicy.setHeightForWidth(self.fader54_2.sizePolicy().hasHeightForWidth())
        self.fader54_2.setSizePolicy(sizePolicy)
        self.fader54_2.setMinimumSize(QSize(0, 190))
        self.fader54_2.setMaximumSize(QSize(15, 190))
        self.fader54_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader54_2.setAutoFillBackground(False)
        self.fader54_2.setMaximum(127)
        self.fader54_2.setSliderPosition(0)
        self.fader54_2.setOrientation(Qt.Orientation.Vertical)
        self.fader54_2.setInvertedAppearance(False)
        self.fader54_2.setInvertedControls(False)

        self.fader54_layout_2.addWidget(self.fader54_2, 0, 0, 1, 1)


        self.below_button_layout_fader54_2.addLayout(self.fader54_layout_2, 0, 0, 1, 1)

        self.pushButton_fader54_2 = QPushButton(self.frame_fader54_2)
        self.pushButton_fader54_2.setObjectName(u"pushButton_fader54_2")

        self.below_button_layout_fader54_2.addWidget(self.pushButton_fader54_2, 2, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader54_2.addItem(self.verticalSpacer_12, 1, 0, 1, 1)


        self.gridLayout_28.addLayout(self.below_button_layout_fader54_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_fader54_2, 10, 7, 1, 1)

        self.frame_fader55_2 = QFrame(self.dockWidgetContents_5)
        self.frame_fader55_2.setObjectName(u"frame_fader55_2")
        self.frame_fader55_2.setMinimumSize(QSize(88, 250))
        self.frame_fader55_2.setMaximumSize(QSize(88, 250))
        self.frame_fader55_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader55_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_fader55_2)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader55_2 = QGridLayout()
        self.below_button_layout_fader55_2.setSpacing(0)
        self.below_button_layout_fader55_2.setObjectName(u"below_button_layout_fader55_2")
        self.pushButton_fader55_2 = QPushButton(self.frame_fader55_2)
        self.pushButton_fader55_2.setObjectName(u"pushButton_fader55_2")

        self.below_button_layout_fader55_2.addWidget(self.pushButton_fader55_2, 2, 0, 1, 1)

        self.fader55_layout_2 = QGridLayout()
        self.fader55_layout_2.setObjectName(u"fader55_layout_2")
        self.fader55_2 = QSlider(self.frame_fader55_2)
        self.fader55_2.setObjectName(u"fader55_2")
        sizePolicy.setHeightForWidth(self.fader55_2.sizePolicy().hasHeightForWidth())
        self.fader55_2.setSizePolicy(sizePolicy)
        self.fader55_2.setMinimumSize(QSize(0, 190))
        self.fader55_2.setMaximumSize(QSize(15, 190))
        self.fader55_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader55_2.setAutoFillBackground(False)
        self.fader55_2.setMaximum(127)
        self.fader55_2.setSliderPosition(0)
        self.fader55_2.setOrientation(Qt.Orientation.Vertical)
        self.fader55_2.setInvertedAppearance(False)
        self.fader55_2.setInvertedControls(False)

        self.fader55_layout_2.addWidget(self.fader55_2, 0, 0, 1, 1)


        self.below_button_layout_fader55_2.addLayout(self.fader55_layout_2, 0, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader55_2.addItem(self.verticalSpacer_11, 1, 0, 1, 1)


        self.gridLayout_29.addLayout(self.below_button_layout_fader55_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_fader55_2, 10, 8, 1, 1)

        self.frame_fader56_2 = QFrame(self.dockWidgetContents_5)
        self.frame_fader56_2.setObjectName(u"frame_fader56_2")
        self.frame_fader56_2.setMinimumSize(QSize(88, 250))
        self.frame_fader56_2.setMaximumSize(QSize(88, 250))
        self.frame_fader56_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader56_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_fader56_2)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader56_2 = QGridLayout()
        self.below_button_layout_fader56_2.setSpacing(0)
        self.below_button_layout_fader56_2.setObjectName(u"below_button_layout_fader56_2")
        self.pushButton_fader56_2 = QPushButton(self.frame_fader56_2)
        self.pushButton_fader56_2.setObjectName(u"pushButton_fader56_2")

        self.below_button_layout_fader56_2.addWidget(self.pushButton_fader56_2, 2, 0, 1, 1)

        self.fader56_layout_2 = QGridLayout()
        self.fader56_layout_2.setObjectName(u"fader56_layout_2")
        self.fader56_2 = QSlider(self.frame_fader56_2)
        self.fader56_2.setObjectName(u"fader56_2")
        sizePolicy.setHeightForWidth(self.fader56_2.sizePolicy().hasHeightForWidth())
        self.fader56_2.setSizePolicy(sizePolicy)
        self.fader56_2.setMinimumSize(QSize(0, 190))
        self.fader56_2.setMaximumSize(QSize(15, 190))
        self.fader56_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader56_2.setAutoFillBackground(False)
        self.fader56_2.setMaximum(127)
        self.fader56_2.setSliderPosition(0)
        self.fader56_2.setOrientation(Qt.Orientation.Vertical)
        self.fader56_2.setInvertedAppearance(False)
        self.fader56_2.setInvertedControls(False)

        self.fader56_layout_2.addWidget(self.fader56_2, 0, 0, 1, 1)


        self.below_button_layout_fader56_2.addLayout(self.fader56_layout_2, 0, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader56_2.addItem(self.verticalSpacer_10, 1, 0, 1, 1)


        self.gridLayout_30.addLayout(self.below_button_layout_fader56_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_fader56_2, 10, 10, 1, 1)

        self.Wing2_dock.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.Wing2_dock)

        self.menubar.addAction(self.menuOpen_new_Wing_View.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuOpen_new_Wing_View.addAction(self.actionWing_1)
        self.menuOpen_new_Wing_View.addAction(self.actionWing_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Am I Dot2 ? - The ultimate Akai-Dot2 Interface", None))
        self.actionWing_1.setText(QCoreApplication.translate("MainWindow", u"Wing-1", None))
        self.actionWing_2.setText(QCoreApplication.translate("MainWindow", u"Wing-2", None))
        self.menuOpen_new_Wing_View.setTitle(QCoreApplication.translate("MainWindow", u"Open new Wing View", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Wing1_dock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wing-1", None))
        self.button36.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.button61.setText(QCoreApplication.translate("MainWindow", u"61", None))
        self.button45.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.button44.setText(QCoreApplication.translate("MainWindow", u"44", None))
        self.button8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button116.setText(QCoreApplication.translate("MainWindow", u"116", None))
        self.button16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.button12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.button10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.button49.setText(QCoreApplication.translate("MainWindow", u"49", None))
        self.button30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.button113.setText(QCoreApplication.translate("MainWindow", u"113", None))
        self.button104.setText(QCoreApplication.translate("MainWindow", u"104", None))
        self.button25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.button63.setText(QCoreApplication.translate("MainWindow", u"63", None))
        self.button122.setText(QCoreApplication.translate("MainWindow", u"122", None))
        self.button48.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.button31.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.button7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button35.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.button39.setText(QCoreApplication.translate("MainWindow", u"39", None))
        self.button24.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.button3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button46.setText(QCoreApplication.translate("MainWindow", u"46", None))
        self.button40.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.button55.setText(QCoreApplication.translate("MainWindow", u"55", None))
        self.button9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button38.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.button100.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.button119.setText(QCoreApplication.translate("MainWindow", u"119", None))
        self.button52.setText(QCoreApplication.translate("MainWindow", u"52", None))
        self.button51.setText(QCoreApplication.translate("MainWindow", u"51", None))
        self.button60.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.button13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.button14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.button6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button26.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button34.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.button117.setText(QCoreApplication.translate("MainWindow", u"117", None))
        self.button115.setText(QCoreApplication.translate("MainWindow", u"115", None))
        self.button62.setText(QCoreApplication.translate("MainWindow", u"62", None))
        self.button58.setText(QCoreApplication.translate("MainWindow", u"58", None))
        self.button29.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.button21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.button43.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.button15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.button32.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.button59.setText(QCoreApplication.translate("MainWindow", u"59", None))
        self.button118.setText(QCoreApplication.translate("MainWindow", u"118", None))
        self.button22.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.button42.setText(QCoreApplication.translate("MainWindow", u"42", None))
        self.button107.setText(QCoreApplication.translate("MainWindow", u"107", None))
        self.button27.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.pushButton_fader52.setText(QCoreApplication.translate("MainWindow", u"button52", None))
        self.button17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.pushButton_fader53.setText(QCoreApplication.translate("MainWindow", u"button53", None))
        self.pushButton_fader49.setText(QCoreApplication.translate("MainWindow", u"button49", None))
        self.button37.setText(QCoreApplication.translate("MainWindow", u"37", None))
        self.button41.setText(QCoreApplication.translate("MainWindow", u"41", None))
        self.button0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button56.setText(QCoreApplication.translate("MainWindow", u"56", None))
        self.button23.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.button54.setText(QCoreApplication.translate("MainWindow", u"54", None))
        self.pushButton_fader48.setText(QCoreApplication.translate("MainWindow", u"button48", None))
        self.button106.setText(QCoreApplication.translate("MainWindow", u"106", None))
        self.button33.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.button28.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.button102.setText(QCoreApplication.translate("MainWindow", u"102", None))
        self.button18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.button19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.button47.setText(QCoreApplication.translate("MainWindow", u"47", None))
        self.button53.setText(QCoreApplication.translate("MainWindow", u"53", None))
        self.button112.setText(QCoreApplication.translate("MainWindow", u"112", None))
        self.button114.setText(QCoreApplication.translate("MainWindow", u"114", None))
        self.button50.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.pushButton_fader51.setText(QCoreApplication.translate("MainWindow", u"button51", None))
        self.pushButton_fader50.setText(QCoreApplication.translate("MainWindow", u"button50", None))
        self.button105.setText(QCoreApplication.translate("MainWindow", u"105", None))
        self.button20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.button101.setText(QCoreApplication.translate("MainWindow", u"101", None))
        self.button103.setText(QCoreApplication.translate("MainWindow", u"103", None))
        self.button57.setText(QCoreApplication.translate("MainWindow", u"57", None))
        self.pushButton_fader54.setText(QCoreApplication.translate("MainWindow", u"button54", None))
        self.pushButton_fader55.setText(QCoreApplication.translate("MainWindow", u"button55", None))
        self.pushButton_fader56.setText(QCoreApplication.translate("MainWindow", u"button56", None))
        self.Wing2_dock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wing-2", None))
        self.button36_2.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.button61_2.setText(QCoreApplication.translate("MainWindow", u"61", None))
        self.button45_2.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.button44_2.setText(QCoreApplication.translate("MainWindow", u"44", None))
        self.button8_2.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button116_2.setText(QCoreApplication.translate("MainWindow", u"116", None))
        self.button16_2.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.button12_2.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.button10_2.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.button49_2.setText(QCoreApplication.translate("MainWindow", u"49", None))
        self.button30_2.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.button113_2.setText(QCoreApplication.translate("MainWindow", u"113", None))
        self.button104_2.setText(QCoreApplication.translate("MainWindow", u"104", None))
        self.button25_2.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.button63_2.setText(QCoreApplication.translate("MainWindow", u"63", None))
        self.button122_2.setText(QCoreApplication.translate("MainWindow", u"122", None))
        self.button48_2.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.button31_2.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.button7_2.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button4_2.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button35_2.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.button39_2.setText(QCoreApplication.translate("MainWindow", u"39", None))
        self.button24_2.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.button3_2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button46_2.setText(QCoreApplication.translate("MainWindow", u"46", None))
        self.button40_2.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.button55_2.setText(QCoreApplication.translate("MainWindow", u"55", None))
        self.button9_2.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button5_2.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button38_2.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.button100_2.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.button119_2.setText(QCoreApplication.translate("MainWindow", u"119", None))
        self.button52_2.setText(QCoreApplication.translate("MainWindow", u"52", None))
        self.button51_2.setText(QCoreApplication.translate("MainWindow", u"51", None))
        self.button60_2.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.button13_2.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.button14_2.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.button6_2.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button26_2.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.button1_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button34_2.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.button117_2.setText(QCoreApplication.translate("MainWindow", u"117", None))
        self.button115_2.setText(QCoreApplication.translate("MainWindow", u"115", None))
        self.button62_2.setText(QCoreApplication.translate("MainWindow", u"62", None))
        self.button58_2.setText(QCoreApplication.translate("MainWindow", u"58", None))
        self.button29_2.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.button21_2.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.button43_2.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.button15_2.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.button32_2.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.button59_2.setText(QCoreApplication.translate("MainWindow", u"59", None))
        self.button118_2.setText(QCoreApplication.translate("MainWindow", u"118", None))
        self.button22_2.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.button42_2.setText(QCoreApplication.translate("MainWindow", u"42", None))
        self.button107_2.setText(QCoreApplication.translate("MainWindow", u"107", None))
        self.button27_2.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.pushButton_fader52_2.setText(QCoreApplication.translate("MainWindow", u"button52", None))
        self.button17_2.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.pushButton_fader53_2.setText(QCoreApplication.translate("MainWindow", u"button53", None))
        self.pushButton_fader49_2.setText(QCoreApplication.translate("MainWindow", u"button49", None))
        self.button37_2.setText(QCoreApplication.translate("MainWindow", u"37", None))
        self.button41_2.setText(QCoreApplication.translate("MainWindow", u"41", None))
        self.button0_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button56_2.setText(QCoreApplication.translate("MainWindow", u"56", None))
        self.button23_2.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.button54_2.setText(QCoreApplication.translate("MainWindow", u"54", None))
        self.pushButton_fader48_2.setText(QCoreApplication.translate("MainWindow", u"button48", None))
        self.button106_2.setText(QCoreApplication.translate("MainWindow", u"106", None))
        self.button33_2.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.button28_2.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.button2_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button11_2.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.button102_2.setText(QCoreApplication.translate("MainWindow", u"102", None))
        self.button18_2.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.button19_2.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.button47_2.setText(QCoreApplication.translate("MainWindow", u"47", None))
        self.button53_2.setText(QCoreApplication.translate("MainWindow", u"53", None))
        self.button112_2.setText(QCoreApplication.translate("MainWindow", u"112", None))
        self.button114_2.setText(QCoreApplication.translate("MainWindow", u"114", None))
        self.button50_2.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.pushButton_fader51_2.setText(QCoreApplication.translate("MainWindow", u"button51", None))
        self.pushButton_fader50_2.setText(QCoreApplication.translate("MainWindow", u"button50", None))
        self.button105_2.setText(QCoreApplication.translate("MainWindow", u"105", None))
        self.button20_2.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.button101_2.setText(QCoreApplication.translate("MainWindow", u"101", None))
        self.button103_2.setText(QCoreApplication.translate("MainWindow", u"103", None))
        self.button57_2.setText(QCoreApplication.translate("MainWindow", u"57", None))
        self.pushButton_fader54_2.setText(QCoreApplication.translate("MainWindow", u"button54", None))
        self.pushButton_fader55_2.setText(QCoreApplication.translate("MainWindow", u"button55", None))
        self.pushButton_fader56_2.setText(QCoreApplication.translate("MainWindow", u"button56", None))
    # retranslateUi

